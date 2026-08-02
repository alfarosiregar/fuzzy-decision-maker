<template>
  <section id="tentang" class="py-20 bg-bakery-100/50 dark:bg-slate-900/50 transition-colors duration-300">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      
      <!-- Section Header -->
      <div class="text-center max-w-3xl mx-auto space-y-4 mb-16">
        <div class="inline-flex items-center space-x-2 px-4 py-2 rounded-full bg-amber-100 dark:bg-amber-950/60 border border-amber-300/50 dark:border-amber-700/50 text-amber-800 dark:text-amber-300 text-xs sm:text-sm font-semibold shadow-sm">
          <Store class="w-4 h-4 text-amber-600 dark:text-amber-400 animate-pulse" />
          <span>Tentang Kami</span>
        </div>
        
        <h2 class="text-3xl sm:text-4xl font-extrabold text-slate-900 dark:text-white tracking-tight">
          Cita Rasa Klasik Donat Kentang
        </h2>
        <p class="text-base sm:text-lg text-slate-600 dark:text-slate-300">
          Donat Kentang Syifa (DKS) didirikan dengan komitmen menyajikan hidangan donat kentang berkualitas tinggi, empuk, higienis, dan sehat bagi konsumen.
        </p>
      </div>

      <!-- Feature Grid -->
      <div class="grid md:grid-cols-2 lg:grid-cols-3 gap-8">
        
        <!-- Card 1 -->
        <div class="bg-white dark:bg-slate-800 p-8 rounded-3xl shadow-sm hover:shadow-xl transition-all duration-300 border border-slate-100 dark:border-slate-700/80 space-y-4">
          <div class="w-14 h-14 rounded-2xl bg-amber-100 dark:bg-amber-950 flex items-center justify-center text-amber-600 dark:text-amber-400">
            <HeartHandshake class="w-7 h-7" />
          </div>
          <h3 class="text-xl font-bold text-slate-900 dark:text-white">Bahan Baku Kentang Pilihan</h3>
          <p class="text-slate-600 dark:text-slate-300 text-sm leading-relaxed">
            Menggunakan kentang kualitas super yang dikukus halus dan dicampur dengan tepung terigu protein tinggi untuk menghasilkan tekstur lembut khas yang tahan lama secara alami.
          </p>
        </div>

        <!-- Card 2 -->
        <div class="bg-white dark:bg-slate-800 p-8 rounded-3xl shadow-sm hover:shadow-xl transition-all duration-300 border border-slate-100 dark:border-slate-700/80 space-y-4">
          <div class="w-14 h-14 rounded-2xl bg-amber-100 dark:bg-amber-950 flex items-center justify-center text-amber-600 dark:text-amber-400">
            <Sparkles class="w-7 h-7" />
          </div>
          <h3 class="text-xl font-bold text-slate-900 dark:text-white">Kualitas Produksi Terjamin</h3>
          <p class="text-slate-600 dark:text-slate-300 text-sm leading-relaxed">
            Setiap donat dibuat dengan resep rahasia dan kontrol mutu ketat agar hasilnya selalu empuk, harum, dan siap dinikmati kapan saja.
          </p>
        </div>

        <!-- Card 3 -->
        <div class="bg-white dark:bg-slate-800 p-8 rounded-3xl shadow-sm hover:shadow-xl transition-all duration-300 border border-slate-100 dark:border-slate-700/80 space-y-4">
          <div class="w-14 h-14 rounded-2xl bg-amber-100 dark:bg-amber-950 flex items-center justify-center text-amber-600 dark:text-amber-400">
            <BarChart3 class="w-7 h-7" />
          </div>
          <h3 class="text-xl font-bold text-slate-900 dark:text-white">Perencanaan Produksi Cermat</h3>
          <p class="text-slate-600 dark:text-slate-300 text-sm leading-relaxed">
            Produksi disesuaikan agar stok selalu siap, sehingga pelanggan mendapat donat segar tanpa menunggu lama.
          </p>
        </div>

      </div>

    </div>
  </section>
</template>

<script setup>
import { HeartHandshake, Sparkles, BarChart3, Store } from 'lucide-vue-next'
</script>