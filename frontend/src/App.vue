<template>
  <div class="min-h-screen flex flex-col selection:bg-amber-500 selection:text-white">
    <!-- Main Top Navigation -->
    <Navbar :is-dark="isDark" @toggle-theme="toggleTheme" />

    <!-- Main Page Sections -->
    <main class="flex-grow">
      <Hero />
      <About />
      <Advantages />
      <ProductShowcase />
      <LocationMap />
    </main>

    <!-- Footer -->
    <Footer />
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import Navbar from './components/Navbar.vue'
import Hero from './components/Hero.vue'
import About from './components/About.vue'
import Advantages from './components/Advantages.vue'
import ProductShowcase from './components/ProductShowcase.vue'
import LocationMap from './components/LocationMap.vue'
import Footer from './components/Footer.vue'

const isDark = ref(false)

const updateThemeClass = () => {
  if (isDark.value) {
    document.documentElement.classList.add('dark')
  } else {
    document.documentElement.classList.remove('dark')
  }
}

const toggleTheme = () => {
  isDark.value = !isDark.value
  localStorage.setItem('dks_theme', isDark.value ? 'dark' : 'light')
  updateThemeClass()
}

onMounted(() => {
  const savedTheme = localStorage.getItem('dks_theme')
  if (savedTheme) {
    isDark.value = savedTheme === 'dark'
  } else {
    isDark.value = window.matchMedia('(prefers-color-scheme: dark)').matches
  }
  updateThemeClass()
})
</script>
