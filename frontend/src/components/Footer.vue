<template>
  <footer class="bg-slate-900 text-slate-300 border-t border-slate-800 transition-colors duration-300">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-16">
      
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-10">
        
        <!-- Col 1: Brand Info -->
        <div class="space-y-4">
          <div class="flex items-center space-x-3 group">
            <div class="flex items-center justify-center group-hover:scale-110 group-hover:rotate-12 transition-all duration-300">
              <span class="text-3xl leading-none animate-bounce-subtle">🍩</span>
            </div>
            <div>
              <span class="text-xl font-extrabold text-white block">
                DKS
              </span>
              <span class="text-xs font-semibold text-amber-400 tracking-wider uppercase block">
                Donat Kentang Syifa
              </span>
            </div>
          </div>
          
          <p class="text-xs sm:text-sm text-slate-400 leading-relaxed">
            Toko donat kentang lembut berkualitas tinggi dengan pelayanan cepat dan varian rasa yang menggoda.
          </p>
        </div>

        <!-- Col 2: Nav Quick Links -->
        <div class="space-y-3">
          <h4 class="text-sm font-bold text-white uppercase tracking-wider">Navigasi Halaman</h4>
          <ul class="space-y-2 text-sm">
            <li><a href="#hero" class="hover:text-amber-400 transition-colors">Beranda</a></li>
            <li><a href="#tentang" class="hover:text-amber-400 transition-colors">Tentang Kami</a></li>
            <li><a href="#keunggulan" class="hover:text-amber-400 transition-colors">Keunggulan DKS</a></li>
            <li><a href="#lokasi" class="hover:text-amber-400 transition-colors">Lokasi Outlet DKS</a></li>
            <li><button @click.prevent="showOrderModal = true" class="hover:text-amber-400 transition-colors cursor-pointer text-left w-full">Pesan Sekarang</button></li>
          </ul>
        </div>

        <!-- Col 3: Operational Hours -->
        <div class="space-y-3">
          <h4 class="text-sm font-bold text-white uppercase tracking-wider">Jam Operasional Outlet Utama</h4>
          <ul class="space-y-2 text-xs sm:text-sm text-slate-400">
            <li class="flex items-center space-x-2">
              <Clock class="w-4 h-4 text-amber-400 shrink-0" />
              <span>Senin - Minggu: 09:00 - 21:00 WIB</span>
            </li>
            <li class="pt-2 text-emerald-400 font-semibold">
              ✔ Donat Digoreng Fresh Setiap Hari
            </li>
            <li class="pt-6">
              <span class="block text-xs font-semibold text-slate-300 uppercase tracking-wider mb-3">Tersedia Juga Di:</span>
              <div class="flex items-center gap-3">
                <a href="https://gofood.link/u/yADZ" target="_blank" class="w-[110px] h-[56px] bg-white rounded-xl shadow hover:-translate-y-1 hover:shadow-md transition-all flex items-center justify-center p-2">
                  <img src="/images/logos/gofood.avif" alt="GoFood" class="h-8 w-auto object-contain" />
                </a>
                <a href="https://r.grab.com/g/6-20260725_134144_393f115b9679409db98e39f9d7475d65_MEXMPS-6-C62CCLKKCUEAEX" target="_blank" class="w-[110px] h-[56px] bg-white rounded-xl shadow hover:-translate-y-1 hover:shadow-md transition-all flex items-center justify-center p-2">
                  <img src="/images/logos/grabfood.avif" alt="GrabFood" class="h-8 w-auto object-contain" />
                </a>
                <a href="https://shopee.co.id/universal-link/now-food/shop/20330511" target="_blank" class="w-[110px] h-[56px] bg-white rounded-xl shadow hover:-translate-y-1 hover:shadow-md transition-all flex items-center justify-center p-2">
                  <img src="/images/logos/shopeefood.avif" alt="ShopeeFood" class="h-10 w-auto object-contain" />
                </a>
              </div>
            </li>
          </ul>
        </div>

        <!-- Col 4: Contact & Social -->
        <div class="space-y-3">
          <h4 class="text-sm font-bold text-white uppercase tracking-wider">Kontak & Lokasi Outlet Utama</h4>
          <ul class="space-y-2.5 text-xs sm:text-sm text-slate-400">
            <li class="flex items-start space-x-2.5">
              <MapPin class="w-4 h-4 text-amber-400 shrink-0 mt-0.5" />
              <span>Jl. Setia Budi No.75, Tj. Rejo, Kec. Medan Sunggal, Kota Medan, Sumatera Utara 20122</span>
            </li>
            <li class="flex items-center space-x-2.5">
              <Phone class="w-4 h-4 text-amber-400 shrink-0" />
              <a href="https://wa.me/6282166525525" target="_blank" class="hover:text-amber-400 transition-colors">0821-6652-5525</a>
            </li>
          </ul>

          <div class="flex items-center space-x-3 pt-3">
            <a href="https://www.instagram.com/dks.medann/" target="_blank" class="w-9 h-9 rounded-xl bg-slate-800 hover:bg-amber-600 text-slate-300 hover:text-white flex items-center justify-center transition-colors">
              <Instagram class="w-4 h-4" />
            </a>
            <a href="https://share.google/HTG0JhEsiRhdfPd9d" target="_blank" class="w-9 h-9 rounded-xl bg-slate-800 hover:bg-amber-600 text-slate-300 hover:text-white flex items-center justify-center transition-colors">
              <Facebook class="w-4 h-4" />
            </a>
          </div>
        </div>

      </div>

      <!-- Bottom Disclaimer -->
      <div class="mt-16 pt-8 border-t border-slate-800 flex flex-col sm:flex-row items-center justify-between text-xs text-slate-500 gap-4">
        <p>© 2026 DKS - Donat Kentang Syifa. All rights reserved.</p>
        <p class="text-center sm:text-right">
          Selalu fresh setiap hari untuk pelanggan setia.
        </p>
      </div>

    </div>

    <!-- Footer Order Modal -->
    <transition name="fade">
      <div v-if="showOrderModal" class="fixed inset-0 z-50 flex items-center justify-center p-4 bg-slate-900/80 backdrop-blur-sm" @click.self="showOrderModal = false">
        <div class="bg-white dark:bg-slate-800 rounded-3xl p-6 sm:p-8 max-w-sm w-full shadow-2xl relative transform transition-all">
          <button @click="showOrderModal = false" class="absolute top-4 right-4 p-2 rounded-full text-slate-400 hover:text-slate-600 hover:bg-slate-100 dark:hover:bg-slate-700 dark:hover:text-slate-200 transition-colors">
            <X class="w-5 h-5" />
          </button>
          
          <div class="text-center mb-6">
            <h3 class="text-xl font-bold text-slate-900 dark:text-white mb-1">Pilih Platform</h3>
            <p class="text-sm text-slate-500 dark:text-slate-400">Pesan Donat Kentang Syifa melalui aplikasi berikut:</p>
          </div>

          <div class="flex flex-col gap-4">
            <a href="https://gofood.link/u/yADZ" target="_blank" class="w-full flex items-center justify-center py-5 px-4 border-2 border-slate-100 dark:border-slate-700 rounded-2xl hover:border-amber-400 dark:hover:border-amber-500 transition-colors bg-slate-50 dark:bg-slate-800/50 group">
              <img src="/images/logos/gofood.avif" alt="GoFood" class="h-10 sm:h-12 w-auto object-contain transition-transform group-hover:scale-105" />
            </a>
            <a href="https://r.grab.com/g/6-20260725_134144_393f115b9679409db98e39f9d7475d65_MEXMPS-6-C62CCLKKCUEAEX" target="_blank" class="w-full flex items-center justify-center py-5 px-4 border-2 border-slate-100 dark:border-slate-700 rounded-2xl hover:border-amber-400 dark:hover:border-amber-500 transition-colors bg-slate-50 dark:bg-slate-800/50 group">
              <img src="/images/logos/grabfood.avif" alt="GrabFood" class="h-10 sm:h-12 w-auto object-contain transition-transform group-hover:scale-105" />
            </a>
            <a href="https://shopee.co.id/universal-link/now-food/shop/20330511" target="_blank" class="w-full flex items-center justify-center py-5 px-4 border-2 border-slate-100 dark:border-slate-700 rounded-2xl hover:border-amber-400 dark:hover:border-amber-500 transition-colors bg-slate-50 dark:bg-slate-800/50 group">
              <img src="/images/logos/shopeefood.avif" alt="ShopeeFood" class="h-[52px] sm:h-[62px] w-auto object-contain transition-transform group-hover:scale-105" />
            </a>
          </div>
        </div>
      </div>
    </transition>
  </footer>
</template>

<script setup>
import { ref } from 'vue'
import { Sparkles, Clock, MapPin, Phone, Mail, Instagram, Facebook, X } from 'lucide-vue-next'

const showOrderModal = ref(false)
</script>

<style scoped>
@keyframes bounceSubtle {
  0%, 100% { transform: translateY(0); }
  50% { transform: translateY(-6px); }
}
.animate-bounce-subtle {
  animation: bounceSubtle 3.5s ease-in-out infinite;
}

.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.3s ease;
}
.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}
</style>