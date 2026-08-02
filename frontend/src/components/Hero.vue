<template>
  <section id="hero" class="relative overflow-hidden pt-12 pb-20 lg:pt-20 lg:pb-28 bg-gradient-to-br from-white via-amber-50/50 to-orange-50/30 dark:from-slate-950 dark:via-slate-900 dark:to-slate-950 animate-gradient-bg" @mousemove="handleMouseMove">
    <!-- Interactive Background Decor Accent Circles -->
    <div 
      class="absolute top-1/4 left-1/3 w-[600px] h-[600px] bg-gradient-to-tr from-amber-400/20 to-orange-500/10 rounded-full blur-3xl -z-10 pointer-events-none transition-transform duration-700 ease-out"
      :style="{ transform: `translate(calc(-50% + ${(mouseX + floatX) * 0.6}px), calc(-50% + ${(mouseY + floatY) * 0.6}px))` }"
    ></div>
    <div 
      class="absolute bottom-1/4 right-1/4 w-[500px] h-[500px] bg-gradient-to-bl from-amber-300/20 to-rose-400/10 rounded-full blur-3xl -z-10 pointer-events-none transition-transform duration-700 ease-out"
      :style="{ transform: `translate(calc(25% - ${(mouseX + floatX) * 0.8}px), calc(25% - ${(mouseY + floatY) * 0.8}px))` }"
    ></div>

    <!-- Floating Interactive Particles -->
    <div class="absolute top-20 left-[10%] text-3xl opacity-50 blur-[1px] pointer-events-none transition-transform duration-700 ease-out" :style="{ transform: `translate(${(mouseX + floatX) * -1.5}px, ${(mouseY + floatY) * -1.5}px) rotate(15deg)` }">🍩</div>
    <div class="absolute bottom-32 left-[20%] text-2xl opacity-40 blur-[2px] pointer-events-none transition-transform duration-700 ease-out" :style="{ transform: `translate(${(mouseX + floatX) * 1.2}px, ${(mouseY + floatY) * 1.2}px) rotate(-25deg)` }">🍩</div>
    <div class="absolute top-[30%] right-[15%] text-4xl opacity-30 blur-[3px] pointer-events-none transition-transform duration-700 ease-out" :style="{ transform: `translate(${(mouseX + floatX) * 1.8}px, ${(mouseY + floatY) * 1.8}px) rotate(45deg)` }">🍩</div>
    <div class="absolute top-[40%] right-[30%] text-xl text-amber-400 opacity-60 pointer-events-none transition-transform duration-700 ease-out" :style="{ transform: `translate(${(mouseX + floatX) * -0.8}px, ${(mouseY + floatY) * -0.8}px)` }">✨</div>

    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="grid lg:grid-cols-12 gap-12 items-center">
        
        <!-- Left Content Header & CTA -->
        <div class="lg:col-span-7 space-y-6 text-center lg:text-left">
          
          <!-- Brand Tag Badge -->
          <div class="inline-flex items-center space-x-2 px-4 py-2 rounded-full bg-amber-100 dark:bg-amber-950/60 border border-amber-300/50 dark:border-amber-700/50 text-amber-800 dark:text-amber-300 text-xs sm:text-sm font-semibold shadow-sm">
            <Sparkles class="w-4 h-4 text-amber-600 dark:text-amber-400 animate-pulse" />
            <span>Selamat datang di Donat Kentang Syifa</span>
          </div>

          <!-- Main Title -->
          <h1 class="text-4xl sm:text-5xl lg:text-6xl font-extrabold tracking-tight text-slate-900 dark:text-white leading-[1.15]">
            Sensasi Donat Kentang Lembut dengan <span class="text-gradient">Rasa Premium Setiap Gigitan</span>
          </h1>

          <!-- Subheadline -->
          <p class="text-lg sm:text-xl text-slate-600 dark:text-slate-300 max-w-2xl mx-auto lg:mx-0 font-normal leading-relaxed">
            Donat Kentang Syifa (DKS) menyajikan donat kentang pilihan yang selalu fresh. Kelezatan khas, pelayanan ramah, dan varian rasa terbaik untuk semua momen.
          </p>

          <!-- Action Buttons -->
          <div class="flex flex-col sm:flex-row items-center justify-center lg:justify-start gap-4 pt-4">
            <a 
              href="#produk" 
              class="group w-full sm:w-auto inline-flex items-center justify-center space-x-3 px-8 py-4 rounded-2xl bg-gradient-to-r from-amber-600 via-amber-500 to-orange-500 hover:from-amber-700 hover:to-orange-600 text-white font-bold text-base shadow-xl shadow-amber-600/30 hover:shadow-amber-600/50 hover:-translate-y-1 transition-all duration-300"
            >
              <div class="w-8 h-8 rounded-xl bg-white/20 backdrop-blur-sm flex items-center justify-center group-hover:scale-110 group-hover:rotate-12 transition-all duration-300 shadow-inner">
                <UtensilsCrossed class="w-4 h-4 text-white" />
              </div>
              <span class="tracking-wide">Lihat Daftar Menu</span>
            </a>
          </div>

          <!-- Quick Stats Banner -->
            <div class="grid grid-cols-3 gap-4 pt-8 border-t border-slate-200 dark:border-slate-800/80">
              <div>
                <div class="text-2xl sm:text-3xl font-extrabold text-amber-600 dark:text-amber-400">100%</div>
                <div class="text-xs sm:text-sm text-slate-500 dark:text-slate-400">Kentang Asli</div>
              </div>
              <div>
                <div class="text-2xl sm:text-3xl font-extrabold text-amber-600 dark:text-amber-400">Fresh</div>
                <div class="text-xs sm:text-sm text-slate-500 dark:text-slate-400">Dibuat Setiap Hari</div>
              </div>
              <div class="relative h-[48px] sm:h-[56px] overflow-hidden">
                <transition name="slide-vertical">
                  <div :key="currentStatIndex" class="absolute inset-0 flex flex-col justify-end pb-1">
                    <div class="text-2xl sm:text-3xl font-extrabold text-amber-600 dark:text-amber-400 flex items-center space-x-1 leading-none mb-1">
                      <span class="text-lg">⭐</span>
                      <span>{{ stats[currentStatIndex].score }}</span>                      
                    </div>
                    <div class="text-xs sm:text-sm text-slate-500 dark:text-slate-400 whitespace-nowrap leading-none">Rating {{ stats[currentStatIndex].platform }}</div>
                  </div>
                </transition>
              </div>
            </div>
        </div>

        <!-- Right Hero Interactive Showcase Container -->
        <div class="lg:col-span-5">
          <div class="relative max-w-md mx-auto">
            
            <!-- Donat Bakery Card Showcase -->
            <div class="glass-card rounded-3xl p-6 sm:p-8 shadow-2xl border border-amber-200/50 dark:border-slate-700/60 relative z-10">
              
              <div class="relative rounded-2xl overflow-hidden mb-6 group bg-amber-500/10 p-8 flex items-center justify-center">
                <div class="w-48 h-48 sm:w-56 sm:h-56 relative flex items-center justify-center">
                  <!-- Animated Donut Illustration SVG -->
                  <div class="text-8xl sm:text-9xl animate-bounce-subtle select-none filter drop-shadow-xl">
                    🍩
                  </div>
                </div>
                <div class="absolute top-4 right-4 bg-emerald-500 text-white text-xs font-bold px-3 py-1 rounded-full shadow">
                  Fresh From The Oven
                </div>
              </div>

              <!-- Product Highlight Preview Card -->
              <div class="bg-slate-900 text-white rounded-2xl p-5 shadow-lg border border-slate-800">
                <div class="flex justify-between items-center mb-1">
                  <div class="flex items-center space-x-2">
                    <span class="w-2.5 h-2.5 rounded-full bg-emerald-400 animate-ping-slow"></span>
                    <span class="text-xs font-bold uppercase tracking-wider text-emerald-400">Best Seller</span>
                  </div>
                  <span class="text-xs text-slate-400">Pilihan Menu Favorit</span>
                </div>

                <div class="space-y-1 text-sm">
                  <div class="flex flex-col items-center justify-center pt-2 pb-2">
                    <span class="font-medium text-amber-400 text-xs sm:text-sm mb-1">Rekomendasi Pilihan:</span>
                    <div class="relative w-full h-8 flex items-center justify-center overflow-hidden">
                      <transition name="slide-horizontal">
                        <div :key="currentBestSellerIndex" class="absolute inset-0 flex justify-center items-center">
                          <span class="text-lg sm:text-xl font-extrabold text-emerald-400 whitespace-nowrap drop-shadow-md">
                            {{ bestSellers[currentBestSellerIndex] }}
                          </span>
                        </div>
                      </transition>
                    </div>
                  </div>
                  <div class="pt-3 border-t border-slate-800 flex justify-center items-center">
                    <span class="text-sm font-semibold text-emerald-400"><span class="inline-block animate-flame origin-bottom">🔥</span> Terjual lebih dari 10rb++ pcs Donat</span>
                  </div>
                </div>
              </div>

            </div>

            <!-- Decorative Floating Card -->
            <div class="absolute -bottom-10 sm:-bottom-12 -left-2 sm:-left-6 bg-white dark:bg-slate-800 p-4 rounded-2xl shadow-xl border border-slate-200 dark:border-slate-700 flex items-center space-x-3 z-20">
              <div class="w-10 h-10 rounded-xl bg-amber-100 dark:bg-amber-950 flex items-center justify-center text-amber-600 dark:text-amber-400 relative overflow-hidden">
                <transition name="slide-vertical">
                  <component :is="floatingIcons[currentFloatingIconIndex]" :key="currentFloatingIconIndex" class="w-5 h-5 absolute inset-0 m-auto" />
                </transition>
              </div>
              <div>
                <div class="text-xs font-bold text-slate-500 dark:text-slate-400">Penjualan Favorit</div>
                <div class="text-sm font-extrabold text-slate-800 dark:text-white">Rekomendasi Pilihan Menu</div>
              </div>
            </div>

          </div>
        </div>

      </div>
    </div>
  </section>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue'
import { Sparkles, ArrowRight, UtensilsCrossed, TrendingUp, LogIn, Star, Heart, Award, ThumbsUp } from 'lucide-vue-next'

const bestSellers = ['Coklat Meises', 'Vanilla Kopi', 'Crumble Matcha', 'Coklat Keju']
const currentBestSellerIndex = ref(0)

const stats = [
  { platform: 'ShopeeFood', score: '4.9' },
  { platform: 'GrabFood', score: '4.8' },
  { platform: 'GoFood', score: '4.9' }
]
const currentStatIndex = ref(0)

const floatingIcons = [TrendingUp, Star, Heart, Award, ThumbsUp]
const currentFloatingIconIndex = ref(0)

// Interactive Mouse Parallax
const mouseX = ref(0)
const mouseY = ref(0)
const floatX = ref(0)
const floatY = ref(0)
const handleMouseMove = (e) => {
  if (typeof window !== 'undefined') {
    mouseX.value = (e.clientX - window.innerWidth / 2) * 0.05
    mouseY.value = (e.clientY - window.innerHeight / 2) * 0.05
  }
}

let intervalId
let animationFrameId

const updateFloating = () => {
  const time = Date.now() / 1500
  floatX.value = Math.sin(time) * 15
  floatY.value = Math.cos(time * 0.8) * 15
  animationFrameId = requestAnimationFrame(updateFloating)
}

onMounted(() => {
  updateFloating()
  intervalId = setInterval(() => {
    currentBestSellerIndex.value = (currentBestSellerIndex.value + 1) % bestSellers.length
    currentStatIndex.value = (currentStatIndex.value + 1) % stats.length
    currentFloatingIconIndex.value = (currentFloatingIconIndex.value + 1) % floatingIcons.length
  }, 3000)
})

onUnmounted(() => {
  if (intervalId) clearInterval(intervalId)
  if (animationFrameId) cancelAnimationFrame(animationFrameId)
})
</script>

<style scoped>
@keyframes bounceSubtle {
  0%, 100% { transform: translateY(0); }
  50% { transform: translateY(-8px); }
}
.animate-bounce-subtle {
  animation: bounceSubtle 4s ease-in-out infinite;
}
.animate-pulse {
  animation: pulse 2s ease-in-out infinite;
}

@keyframes pingSlow {
  75%, 100% {
    transform: scale(2);
    opacity: 0;
  }
}
.animate-ping-slow {
  animation: pingSlow 2.5s cubic-bezier(0, 0, 0.2, 1) infinite;
}

@keyframes flame {
  0%, 100% { transform: rotate(-10deg) scale(1); }
  50% { transform: rotate(10deg) scale(1.2); }
}
.animate-flame {
  animation: flame 1.5s ease-in-out infinite;
}

@keyframes gradient-bg {
  0% { background-position: 0% 50%; }
  50% { background-position: 100% 50%; }
  100% { background-position: 0% 50%; }
}
.animate-gradient-bg {
  background-size: 200% 200%;
  animation: gradient-bg 15s ease infinite;
}

/* Horizontal Slide for Best Seller */
.slide-horizontal-enter-active,
.slide-horizontal-leave-active {
  transition: all 0.5s ease;
}
.slide-horizontal-enter-from {
  opacity: 0;
  transform: translateX(20px);
}
.slide-horizontal-leave-to {
  opacity: 0;
  transform: translateX(-20px);
}

/* Vertical Slide for Stats */
.slide-vertical-enter-active,
.slide-vertical-leave-active {
  transition: all 0.5s ease;
}
.slide-vertical-enter-from {
  opacity: 0;
  transform: translateY(20px);
}
.slide-vertical-leave-to {
  opacity: 0;
  transform: translateY(-20px);
}
</style>