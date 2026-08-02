"""
Fuzzy Inference System (FIS) Mamdani implementation for UMKM Donat Kentang Syifa (DKS).
Handles fuzzification, rule evaluation (min implication, max aggregation), 
centroid defuzzification, and interactive visualization charts.
"""

import numpy as np
import plotly.graph_objects as go
from config import DOMAIN_PERMINTAAN, DOMAIN_PERSEDIAAN, DOMAIN_PRODUKSI, FUZZY_PARAMS, MAMDANI_RULES


def trimf(x, params):
    """
    Triangular Membership Function.
    params: [a, b, c] where a <= b <= c
    """
    a, b, c = params
    x = np.asarray(x, dtype=float)
    y = np.zeros_like(x)

    # Left slope
    if b > a:
        idx_left = np.logical_and(a <= x, x < b)
        y[idx_left] = (x[idx_left] - a) / (b - a)
    elif a == b:
        idx_left = (x == a)
        y[idx_left] = 1.0

    # Right slope
    if c > b:
        idx_right = np.logical_and(b <= x, x <= c)
        y[idx_right] = (c - x[idx_right]) / (c - b)
    elif b == c:
        idx_right = (x == b)
        y[idx_right] = 1.0

    # Peak point
    y[x == b] = 1.0

    return np.clip(y, 0.0, 1.0)


def trapmf(x, params):
    """
    Trapezoidal Membership Function.
    params: [a, b, c, d] where a <= b <= c <= d
    """
    a, b, c, d = params
    x = np.asarray(x, dtype=float)
    y = np.zeros_like(x)

    # Left ramp
    if b > a:
        idx_left = np.logical_and(a <= x, x < b)
        y[idx_left] = (x[idx_left] - a) / (b - a)
    else: # a == b
        idx_left = (x >= a)
        y[idx_left] = 1.0

    # Plateau
    idx_plateau = np.logical_and(b <= x, x <= c)
    y[idx_plateau] = 1.0

    # Right ramp
    if d > c:
        idx_right = np.logical_and(c < x, x <= d)
        y[idx_right] = (d - x[idx_right]) / (d - c)
    else: # c == d
        idx_right = (x <= c)

    return np.clip(y, 0.0, 1.0)


def calculate_mf(x, mf_def):
    """Helper to calculate membership value given type and params."""
    mf_type = mf_def["type"]
    params = mf_def["params"]
    if mf_type == "tri":
        return trimf(x, params)
    elif mf_type == "trap":
        return trapmf(x, params)
    else:
        raise ValueError(f"Unsupported membership function type: {mf_type}")


class FIS_Mamdani_DKS:
    """
    Fuzzy Inference System Mamdani for Donut Production DSS.
    # Force reload modules
    """

    def __init__(self, fuzzy_params=None, rules=None):
        self.params = fuzzy_params or FUZZY_PARAMS
        self.rules = rules or MAMDANI_RULES

    def fuzzify_variable(self, var_name, value):
        """
        Calculates membership degrees for a given variable value.
        """
        var_config = self.params[var_name]
        degrees = {}
        for set_name, mf_def in var_config.items():
            degrees[set_name] = float(calculate_mf(value, mf_def))
        return degrees

    def evaluate_rules(self, mu_permintaan, mu_persediaan):
        """
        Evaluates Mamdani rules using MIN operator for AND conditions.
        Returns detailed rule execution results and maximum firing strength per output set.
        """
        rule_results = []
        output_strengths = {k: 0.0 for k in self.params["produksi"].keys()}

        for idx, rule in enumerate(self.rules, 1):
            p_set = rule["permintaan"]
            s_set = rule["persediaan"]
            out_set = rule["produksi"]

            degree_p = mu_permintaan.get(p_set, 0.0)
            degree_s = mu_persediaan.get(s_set, 0.0)
            
            # Mamdani MIN operator for AND implication
            firing_strength = min(degree_p, degree_s)

            # MAX aggregation for output sets
            output_strengths[out_set] = max(output_strengths[out_set], firing_strength)

            rule_results.append({
                "rule_no": idx,
                "text": f"IF Permintaan IS {p_set} AND Persediaan IS {s_set} THEN Produksi IS {out_set}",
                "firing_strength": round(firing_strength, 4),
                "output_set": out_set
            })

        return rule_results, output_strengths

    def defuzzify_centroid(self, output_strengths, num_points=1000):
        """
        Defuzzification using Centroid (Center of Gravity) Method over continuous output domain.
        Formula: x_crisp = sum(x * mu(x)) / sum(mu(x))
        """
        x_domain = np.linspace(DOMAIN_PRODUKSI[0], DOMAIN_PRODUKSI[1], num_points)
        aggregated_mf = np.zeros_like(x_domain)

        # Clip output membership functions at firing strength and aggregate using MAX
        for set_name, strength in output_strengths.items():
            if strength > 0:
                mf_def = self.params["produksi"][set_name]
                mf_vals = calculate_mf(x_domain, mf_def)
                clipped_mf = np.minimum(mf_vals, strength)
                aggregated_mf = np.maximum(aggregated_mf, clipped_mf)

        # Centroid calculation
        sum_area = np.sum(aggregated_mf)
        if sum_area == 0:
            # Fallback to midpoint of domain if no rules fired
            crisp_val = (DOMAIN_PRODUKSI[0] + DOMAIN_PRODUKSI[1]) / 2.0
        else:
            crisp_val = np.sum(x_domain * aggregated_mf) / sum_area

        return crisp_val, x_domain, aggregated_mf

    def compute(self, permintaan, persediaan):
        """
        Full FIS Pipeline: Fuzzification -> Inference -> Defuzzification.
        Returns crisp integer production recommendation and full diagnostic data.
        """
        # Step 1: Fuzzification
        mu_permintaan = self.fuzzify_variable("permintaan", permintaan)
        mu_persediaan = self.fuzzify_variable("persediaan", persediaan)

        # Step 2: Rule Evaluation
        rule_results, output_strengths = self.evaluate_rules(mu_permintaan, mu_persediaan)

        # Step 3: Defuzzification
        crisp_float, x_domain, aggregated_mf = self.defuzzify_centroid(output_strengths)
        crisp_int = int(round(crisp_float))

        return {
            "permintaan": permintaan,
            "persediaan": persediaan,
            "produksi_prediksi": crisp_int,
            "produksi_float": round(crisp_float, 2),
            "mu_permintaan": mu_permintaan,
            "mu_persediaan": mu_persediaan,
            "output_strengths": output_strengths,
            "rule_results": rule_results,
            "x_domain": x_domain,
            "aggregated_mf": aggregated_mf
        }

    # --- Plotly Visualization Methods ---
    def plot_membership_functions(self, var_name, current_val=None):
        """
        Generates interactive Plotly figure for variable membership functions.
        """
        if var_name == "permintaan":
            domain = DOMAIN_PERMINTAAN
            title = "Membership Functions - Permintaan (Demand)"
            x_label = "Jumlah Permintaan (Buah)"
        elif var_name == "persediaan":
            domain = DOMAIN_PERSEDIAAN
            title = "Membership Functions - Persediaan (Stock)"
            x_label = "Jumlah Persediaan (Buah)"
        else:
            domain = DOMAIN_PRODUKSI
            title = "Membership Functions - Produksi (Production)"
            x_label = "Jumlah Produksi (Buah)"

        x = np.linspace(domain[0], domain[1], 500)
        fig = go.Figure()

        colors = {"Rendah": "#EF553B", "Sedikit": "#EF553B", "Berkurang": "#EF553B",
                  "Sedang": "#FECB52", "Tetap": "#FECB52",
                  "Tinggi": "#00CC96", "Banyak": "#00CC96", "Bertambah": "#00CC96"}

        for set_name, mf_def in self.params[var_name].items():
            y = calculate_mf(x, mf_def)
            color = colors.get(set_name, "#636EFA")
            fig.add_trace(go.Scatter(
                x=x, y=y,
                mode='lines',
                name=set_name,
                line=dict(width=3, color=color),
                hovertemplate=f"Set: {set_name}<br>Value: %{{x:.1f}}<br>μ: %{{y:.2f}}<extra></extra>"
            ))

        # Add vertical reference line if input provided
        if current_val is not None:
            fig.add_vline(
                x=current_val,
                line_dash="dash",
                line_color="#AB63FA",
                line_width=2,
                annotation_text=f"Input: {current_val}",
                annotation_position="top right"
            )

        fig.update_layout(
            title=title,
            xaxis_title=x_label,
            yaxis_title="Degree of Membership (μ)",
            yaxis=dict(range=[-0.05, 1.05]),
            template="plotly_dark",
            legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
            margin=dict(l=40, r=40, t=60, b=40)
        )
        return fig

    def plot_aggregated_output(self, result_dict):
        """
        Plots aggregated output fuzzy set area and defuzzified centroid line.
        """
        x = result_dict["x_domain"]
        y = result_dict["aggregated_mf"]
        crisp_val = result_dict["produksi_float"]

        fig = go.Figure()
        fig.add_trace(go.Scatter(
            x=x, y=y,
            fill='tozeroy',
            mode='lines',
            name="Aggregated Fuzzy Set",
            line=dict(color="#00CC96", width=2),
            fillcolor="rgba(0, 204, 150, 0.3)",
            hovertemplate="Produksi: %{x:.1f}<br>μ: %{y:.2f}<extra></extra>"
        ))

        # Add Centroid indicator line
        fig.add_vline(
            x=crisp_val,
            line_dash="solid",
            line_color="#FFA15A",
            line_width=3,
            annotation_text=f"Centroid (Prediksi): {result_dict['produksi_prediksi']} unit",
            annotation_position="top right"
        )

        fig.update_layout(
            title="Hasil Defuzzifikasi Centroid (Mamdani Aggregated Output)",
            xaxis_title="Rekomendasi Produksi (Buah)",
            yaxis_title="Degree of Membership (μ)",
            yaxis=dict(range=[-0.05, 1.05]),
            template="plotly_dark",
            margin=dict(l=40, r=40, t=60, b=40)
        )
        return fig
