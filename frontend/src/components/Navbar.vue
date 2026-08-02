<template>
  <nav class="sticky top-0 z-50 glass-nav border-b border-bakery-100 dark:border-slate-800 transition-colors duration-300">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="flex items-center justify-between h-20">
        <!-- Logo & Brand Name -->
        <a href="#" class="flex items-center space-x-3 group">
          <div class="flex items-center justify-center group-hover:scale-110 group-hover:rotate-12 transition-all duration-300">
            <span class="text-3xl leading-none animate-bounce-subtle">🍩</span>
          </div>
          <div>
            <span class="text-xl font-extrabold tracking-tight text-slate-900 dark:text-white block group-hover:text-amber-600 dark:group-hover:text-amber-400 transition-colors">
              DKS
            </span>
            <span class="text-xs font-semibold text-amber-600 dark:text-amber-400 tracking-wider uppercase">
              Donat Kentang Syifa
            </span>
          </div>
        </a>

        <!-- Desktop Navigation Links -->
        <div class="hidden md:flex items-center space-x-8">
          <a href="#hero" class="text-sm font-medium text-slate-700 dark:text-slate-300 hover:text-amber-600 dark:hover:text-amber-400 transition-colors">
            Beranda
          </a>
          <a href="#tentang" class="text-sm font-medium text-slate-700 dark:text-slate-300 hover:text-amber-600 dark:hover:text-amber-400 transition-colors">
            Tentang Kami
          </a>
          <a href="#keunggulan" class="text-sm font-medium text-slate-700 dark:text-slate-300 hover:text-amber-600 dark:hover:text-amber-400 transition-colors">
            Keunggulan
          </a>
          <a href="#lokasi" class="text-sm font-medium text-slate-700 dark:text-slate-300 hover:text-amber-600 dark:hover:text-amber-400 transition-colors">
            Lokasi Toko
          </a>
        </div>

        <!-- Action Controls & Theme Toggle -->
        <div class="hidden md:flex items-center space-x-4">
          <!-- Theme Switcher Button -->
          <button 
            @click="$emit('toggle-theme')" 
            class="p-2.5 rounded-xl bg-bakery-100 dark:bg-slate-800 text-slate-700 dark:text-slate-200 hover:bg-amber-100 dark:hover:bg-slate-700 transition-colors"
            :title="isDark ? 'Switch to Light Mode' : 'Switch to Dark Mode'"
            aria-label="Toggle theme"
          >
            <Sun v-if="isDark" class="w-5 h-5 text-amber-400" />
            <Moon v-else class="w-5 h-5 text-slate-700" />
          </button>

          <!-- Primary CTA Button -->
          <a 
            href="/app" 
            class="inline-flex items-center space-x-2 px-5 py-2.5 rounded-xl bg-gradient-to-r from-amber-600 to-amber-500 hover:from-amber-700 hover:to-amber-600 text-white font-semibold text-sm shadow-lg shadow-amber-600/25 hover:shadow-amber-600/40 hover:-translate-y-0.5 transition-all duration-300"
          >
            <LogIn class="w-4 h-4" />
            <span>Login</span>
          </a>
        </div>

        <!-- Mobile menu toggle button -->
        <div class="flex items-center space-x-2 md:hidden">
          <button 
            @click="$emit('toggle-theme')" 
            class="p-2 rounded-xl bg-bakery-100 dark:bg-slate-800 text-slate-700 dark:text-slate-200"
          >
            <Sun v-if="isDark" class="w-5 h-5 text-amber-400" />
            <Moon v-else class="w-5 h-5 text-slate-700" />
          </button>
          
          <button 
            @click="isMobileMenuOpen = !isMobileMenuOpen" 
            class="p-2.5 rounded-xl bg-bakery-100 dark:bg-slate-800 text-slate-700 dark:text-slate-200"
          >
            <Menu v-if="!isMobileMenuOpen" class="w-6 h-6" />
            <X v-else class="w-6 h-6" />
          </button>
        </div>
      </div>
    </div>

    <!-- Mobile Navigation Drawer -->
    <div v-if="isMobileMenuOpen" class="md:hidden border-b border-slate-200 dark:border-slate-800 bg-bakery-50 dark:bg-slate-900 px-4 pt-3 pb-6 space-y-3">
      <a 
        href="#hero" 
        @click="isMobileMenuOpen = false" 
        class="block py-2 text-slate-700 dark:text-slate-200 font-medium hover:text-amber-600"
      >
        Beranda
      </a>
      <a 
        href="#tentang" 
        @click="isMobileMenuOpen = false" 
        class="block py-2 text-slate-700 dark:text-slate-200 font-medium hover:text-amber-600"
      >
        Tentang Kami
      </a>
      <a 
        href="#keunggulan" 
        @click="isMobileMenuOpen = false" 
        class="block py-2 text-slate-700 dark:text-slate-200 font-medium hover:text-amber-600"
      >
        Keunggulan
      </a>
      <a 
        href="#lokasi" 
        @click="isMobileMenuOpen = false" 
        class="block py-2 text-slate-700 dark:text-slate-200 font-medium hover:text-amber-600"
      >
        Lokasi Toko
      </a>
      <a 
        href="/app" 
        class="flex items-center justify-center space-x-2 w-full mt-4 px-4 py-3 rounded-xl bg-amber-600 text-white font-semibold shadow-md"
      >
        <LogIn class="w-4 h-4" />
        <span>Login</span>
      </a>
    </div>
  </nav>
</template>

<script setup>
import { ref } from 'vue'
import { Sparkles, Sun, Moon, Menu, X, ExternalLink, LogIn } from 'lucide-vue-next'

defineProps({
  isDark: {
    type: Boolean,
    default: false
  }
})

const isMobileMenuOpen = ref(false)
</script>

<style scoped>
@keyframes bounceSubtle {
  0%, 100% { transform: translateY(0); }
  50% { transform: translateY(-6px); }
}
.animate-bounce-subtle {
  animation: bounceSubtle 3.5s ease-in-out infinite;
}
</style>