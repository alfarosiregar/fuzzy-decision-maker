/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{vue,js,ts,jsx,tsx}",
  ],
  darkMode: 'class',
  theme: {
    extend: {
      colors: {
        bakery: {
          50: '#fdf8f6',
          100: '#f2e8e5',
          200: '#e4d1cb',
          300: '#d0b2a7',
          400: '#b88b7d',
          500: '#a36b5b',
          600: '#8c5344',
          700: '#734135',
          800: '#5f372d',
          900: '#4f3028',
          950: '#2b1713',
        },
        amber: {
          50: '#fffbeb',
          100: '#fef3c7',
          500: '#f59e0b',
          600: '#d97706',
          700: '#b45309',
        },
        gold: {
          400: '#fbbf24',
          500: '#f59e0b',
        }
      },
      fontFamily: {
        sans: ['Plus Jakarta Sans', 'Inter', 'sans-serif'],
      },
      boxShadow: {
        'soft': '0 10px 30px -10px rgba(140, 83, 68, 0.15)',
        'glow': '0 0 25px rgba(217, 119, 6, 0.35)',
      }
    },
  },
  plugins: [],
}
