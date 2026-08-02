<template>
  <section id="keunggulan" class="py-20 bg-white dark:bg-slate-950 transition-colors duration-300">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      
      <!-- Section Header -->
      <div class="text-center max-w-3xl mx-auto space-y-4 mb-16">
        <div class="inline-flex items-center space-x-2 px-4 py-2 rounded-full bg-amber-100 dark:bg-amber-950/60 border border-amber-300/50 dark:border-amber-700/50 text-amber-800 dark:text-amber-300 text-xs sm:text-sm font-semibold shadow-sm">
          <Star class="w-4 h-4 text-amber-600 dark:text-amber-400 animate-pulse" />
          <span>Keunggulan Utama</span>
        </div>
        
        <h2 class="text-3xl sm:text-4xl lg:text-5xl font-extrabold text-slate-900 dark:text-white tracking-tight">
          Mengapa Memilih <span class="text-gradient">DKS</span>
        </h2>
        
        <p class="text-base sm:text-lg text-slate-600 dark:text-slate-300 leading-relaxed">
          Kualitas bahan kentang asli premium, tekstur super lembut, dan cita rasa khas yang selalu disajikan segar setiap hari.
        </p>
      </div>

      <div class="grid lg:grid-cols-12 gap-12 items-center">
        
        <!-- Left Banner Image/Illustration -->
        <div class="lg:col-span-5">
          <div class="relative rounded-3xl overflow-hidden bg-gradient-to-tr from-amber-600 to-amber-500 p-8 sm:p-10 text-white shadow-2xl">
            <div class="space-y-6">
              <span class="inline-block px-3 py-1 bg-white/20 backdrop-blur-md rounded-full text-xs font-bold uppercase tracking-wider">
                Keunggulan Utama DKS
              </span>

              <h3 class="text-3xl font-extrabold leading-tight">
                Mengapa Memilih Donat Kentang Syifa?
              </h3>

              <p class="text-white/90 text-sm leading-relaxed">
                Kami menggabungkan bahan-bahan alami segar tanpa pengawet dengan sistem kontrol produksi digital modern.
              </p>

              <div class="space-y-3 pt-4">
                <div v-for="(item, idx) in keyHighlights" :key="idx" class="flex items-center space-x-3 text-sm font-semibold">
                  <CheckCircle2 class="w-5 h-5 text-amber-200 shrink-0" />
                  <span>{{ item }}</span>
                </div>
              </div>
            </div>
          </div>
        </div>

        <!-- Right Advantages Grid -->
        <div class="lg:col-span-7">
          <div class="grid sm:grid-cols-2 gap-6">
            
            <div 
              v-for="(adv, index) in advantagesList" 
              :key="index" 
              class="p-6 rounded-2xl bg-bakery-50 dark:bg-slate-900 border border-slate-200/60 dark:border-slate-800 hover:border-amber-500/50 transition-all duration-300 space-y-3"
            >
              <div class="w-12 h-12 rounded-xl bg-amber-100 dark:bg-amber-950 flex items-center justify-center text-amber-600 dark:text-amber-400">
                <component :is="adv.icon" class="w-6 h-6" />
              </div>
              <h4 class="text-lg font-bold text-slate-900 dark:text-white">{{ adv.title }}</h4>
              <p class="text-slate-600 dark:text-slate-400 text-xs sm:text-sm leading-relaxed">
                {{ adv.description }}
              </p>
            </div>

          </div>
        </div>

      </div>

    </div>
  </section>
</template>

<script setup>
import { CheckCircle2, Flame, Award, Clock, ShieldCheck, Star } from 'lucide-vue-next'

const keyHighlights = [
  "100% Menggunakan Kentang Asli Organik",
  "Tekstur Super Empuk & Tidak Berminyak",
  "Bebas Bahan Pengawet & Pewarna Sintetis",
  "Diproses Secara Higienis & 100% Halal"
]

const advantagesList = [
  {
    icon: Flame,
    title: "Fresh From The Oven",
    description: "Semua donat dibuat dan digoreng hangat setiap hari, memastikan Anda selalu mendapatkan cita rasa terbaik saat dinikmati."
  },
  {
    icon: Award,
    title: "Kualitas Premium",
    description: "Diproduksi dengan standar higienis tinggi menggunakan bahan-bahan grade premium."
  },
    {
    icon: ShieldCheck,
    title: "Produk Halal",
    description: "Terjamin 100% Halal, aman, dan thoyyib. Diproses dengan standar kebersihan untuk kenyamanan Anda."
  },
  {
    icon: Clock,
    title: "Kelembutan Tahan Lama",
    description: "Kandungan kentang yang optimal membuat donat tetap empuk dan lezat hingga 3 hari."
  }
]
</script>
