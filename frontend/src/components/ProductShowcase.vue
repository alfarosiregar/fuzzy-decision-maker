<template>
  <section id="produk" class="py-20 bg-gradient-to-br from-amber-50/40 via-white to-orange-50/30 dark:from-slate-900 dark:via-slate-900/80 dark:to-slate-950 animate-gradient-bg transition-colors duration-300 relative overflow-hidden" @mousemove="handleMouseMove">
    <!-- Interactive Background Blobs -->
    <div 
      class="absolute top-0 left-0 w-[500px] h-[500px] bg-amber-400/10 rounded-full blur-3xl -z-10 pointer-events-none transition-transform duration-700 ease-out"
      :style="{ transform: `translate(${(mouseX + floatX) * 0.5}px, ${(mouseY + floatY) * 0.5}px)` }"
    ></div>
    <div 
      class="absolute bottom-0 right-0 w-[600px] h-[600px] bg-orange-500/10 rounded-full blur-3xl -z-10 pointer-events-none transition-transform duration-700 ease-out"
      :style="{ transform: `translate(${(mouseX + floatX) * -0.6}px, ${(mouseY + floatY) * -0.6}px)` }"
    ></div>

    <!-- Floating Interactive Particles -->
    <div class="absolute top-40 left-[5%] text-3xl opacity-30 blur-[1px] pointer-events-none transition-transform duration-700 ease-out z-0" :style="{ transform: `translate(${(mouseX + floatX) * -1.2}px, ${(mouseY + floatY) * -1.2}px) rotate(15deg)` }">🍩</div>
    <div class="absolute top-[10%] left-[20%] text-2xl opacity-20 blur-[2px] pointer-events-none transition-transform duration-700 ease-out z-0" :style="{ transform: `translate(${(mouseX + floatX) * 1.3}px, ${(mouseY + floatY) * 1.3}px) rotate(30deg)` }">🍩</div>
    <div class="absolute top-[50%] left-[2%] text-4xl opacity-15 blur-[3px] pointer-events-none transition-transform duration-700 ease-out z-0" :style="{ transform: `translate(${(mouseX + floatX) * -1.5}px, ${(mouseY + floatY) * -1.5}px) rotate(-15deg)` }">🍩</div>
    <div class="absolute bottom-[10%] left-[25%] text-5xl opacity-10 blur-[4px] pointer-events-none transition-transform duration-700 ease-out z-0" :style="{ transform: `translate(${(mouseX + floatX) * 2.0}px, ${(mouseY + floatY) * 2.0}px) rotate(70deg)` }">🍩</div>
    
    <div class="absolute bottom-[30%] left-[8%] text-2xl text-amber-400 opacity-40 blur-[1px] pointer-events-none transition-transform duration-700 ease-out z-0" :style="{ transform: `translate(${(mouseX + floatX) * 1.5}px, ${(mouseY + floatY) * 1.5}px) rotate(-25deg)` }">✨</div>
    
    <div class="absolute top-[30%] right-[5%] text-4xl opacity-20 blur-[2px] pointer-events-none transition-transform duration-700 ease-out z-0" :style="{ transform: `translate(${(mouseX + floatX) * 1.1}px, ${(mouseY + floatY) * 1.1}px) rotate(45deg)` }">🍩</div>
    <div class="absolute top-[15%] right-[25%] text-3xl opacity-25 blur-[1.5px] pointer-events-none transition-transform duration-700 ease-out z-0" :style="{ transform: `translate(${(mouseX + floatX) * -0.8}px, ${(mouseY + floatY) * -0.8}px) rotate(-40deg)` }">🍩</div>
    <div class="absolute top-[60%] right-[3%] text-2xl opacity-35 blur-[1px] pointer-events-none transition-transform duration-700 ease-out z-0" :style="{ transform: `translate(${(mouseX + floatX) * 1.4}px, ${(mouseY + floatY) * 1.4}px) rotate(120deg)` }">🍩</div>
    <div class="absolute bottom-[5%] right-[20%] text-4xl opacity-15 blur-[2.5px] pointer-events-none transition-transform duration-700 ease-out z-0" :style="{ transform: `translate(${(mouseX + floatX) * -1.6}px, ${(mouseY + floatY) * -1.6}px) rotate(-60deg)` }">🍩</div>
    
    <div class="absolute bottom-40 right-[10%] text-2xl text-amber-500 opacity-30 pointer-events-none transition-transform duration-700 ease-out z-0" :style="{ transform: `translate(${(mouseX + floatX) * -0.9}px, ${(mouseY + floatY) * -0.9}px)` }">✨</div>

    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10">
      
      <!-- Section Header -->
      <div class="text-center max-w-3xl mx-auto mb-12 space-y-4">
        <div class="inline-flex items-center space-x-2 px-4 py-2 rounded-full bg-amber-100 dark:bg-amber-950/60 border border-amber-300/50 dark:border-amber-700/50 text-amber-800 dark:text-amber-300 text-xs sm:text-sm font-semibold shadow-sm">
          <UtensilsCrossed class="w-4 h-4 text-amber-600 dark:text-amber-400" />
          <span>Daftar Menu</span>
        </div>

        <h2 class="text-3xl sm:text-4xl lg:text-5xl font-extrabold text-slate-900 dark:text-white tracking-tight">
          Daftar Menu <span class="text-gradient">DKS</span>
        </h2>

        <p class="text-base sm:text-lg text-slate-600 dark:text-slate-300 leading-relaxed mb-6">
          Nikmati aneka varian menu DKS yang lezat, dibuat segar setiap hari dengan tekstur lembut yang khas.
        </p>

        <!-- Search Input -->
        <div class="pt-2 pb-6">
          <div class="relative max-w-md mx-auto">
            <input 
              type="text" 
              v-model="searchQuery"
              placeholder="Cari menu donat favoritmu..." 
              class="w-full px-5 py-3 pl-12 rounded-full border border-slate-200 dark:border-slate-700 bg-white dark:bg-slate-800 text-slate-900 dark:text-white focus:outline-none focus:border-amber-500 focus:ring-2 focus:ring-amber-500/20 transition-all shadow-sm text-sm"
            >
            <Search class="w-5 h-5 text-slate-400 absolute left-4 top-1/2 -translate-y-1/2" />
            <button 
              v-if="searchQuery" 
              @click="searchQuery = ''" 
              class="absolute right-4 top-1/2 -translate-y-1/2 text-slate-400 hover:text-slate-600 dark:hover:text-slate-200"
            >
              <X class="w-4 h-4" />
            </button>
          </div>
        </div>

        <!-- Category Filter Tabs -->
        <div class="flex flex-wrap items-center justify-center gap-2">
          <button 
            v-for="cat in categories" 
            :key="cat"
            @click="activeCategory = cat"
            class="px-5 py-2.5 rounded-full text-xs sm:text-sm font-semibold transition-all duration-300"
            :class="activeCategory === cat ? 'bg-amber-600 text-white shadow-md shadow-amber-600/20' : 'bg-white dark:bg-slate-800 text-slate-600 dark:text-slate-300 hover:bg-amber-100 dark:hover:bg-slate-700'"
          >
            {{ cat }}
          </button>
        </div>
      </div>

      <!-- Products Grid -->
      <div class="grid sm:grid-cols-2 lg:grid-cols-3 gap-8">
        <transition-group name="fade">
          <ProductCard 
            v-for="item in displayedProducts" 
            :key="item.id" 
            :product="item" 
            @order="handleOrder"
          />
        </transition-group>
      </div>

      <!-- Lihat Semua Menu Button -->
      <div class="mt-10 text-center" v-if="filteredProducts.length > 9">
        <button 
          @click="showAll = !showAll"
          class="inline-flex items-center space-x-2 px-8 py-3.5 rounded-full font-bold text-sm transition-all duration-300 border-2"
          :class="showAll 
            ? 'bg-white dark:bg-slate-800 text-amber-600 border-amber-400 hover:bg-amber-50 dark:hover:bg-slate-700' 
            : 'bg-gradient-to-r from-amber-500 to-amber-600 text-white border-transparent hover:from-amber-600 hover:to-amber-700 shadow-lg shadow-amber-500/25'"
        >
          <ChevronDown 
            class="w-5 h-5 transition-transform duration-300" 
            :class="showAll ? 'rotate-180' : ''"
          />
          <span>{{ showAll ? 'Tampilkan Lebih Sedikit' : `Lihat Semua Menu (${filteredProducts.length})` }}</span>
        </button>
      </div>

      <!-- Pesan via Platform -->
      <div class="mt-16 text-center max-w-3xl mx-auto">
        <h4 class="text-lg font-bold text-slate-900 dark:text-white mb-2">Pesan Juga Via Platform Favorit Anda</h4>
        <p class="text-sm text-slate-500 dark:text-slate-400 mb-6">Klik logo di bawah untuk langsung memesan melalui aplikasi delivery favorit Anda.</p>
        <div class="flex flex-wrap items-center justify-center gap-6 sm:gap-8">
          <a href="https://gofood.link/u/yADZ" target="_blank" class="group transition-transform duration-300 hover:scale-105 block">
            <img src="/images/logos/gofood.avif" alt="GoFood" class="h-10 sm:h-14 w-auto object-contain drop-shadow-sm group-hover:drop-shadow-md transition-shadow duration-300 rounded-xl" />
          </a>
          <a href="https://r.grab.com/g/6-20260725_134144_393f115b9679409db98e39f9d7475d65_MEXMPS-6-C62CCLKKCUEAEX" target="_blank" class="group transition-transform duration-300 hover:scale-105 block">
            <img src="/images/logos/grabfood.avif" alt="GrabFood" class="h-10 sm:h-14 w-auto object-contain drop-shadow-sm group-hover:drop-shadow-md transition-shadow duration-300 rounded-xl" />
          </a>
          <a href="https://shopee.co.id/universal-link/now-food/shop/20330511" target="_blank" class="group transition-transform duration-300 hover:scale-105 block">
            <img src="/images/logos/shopeefood.avif" alt="ShopeeFood" class="h-[52px] sm:h-[72px] w-auto object-contain drop-shadow-sm group-hover:drop-shadow-md transition-shadow duration-300 rounded-xl" />
          </a>
        </div>
      </div>

      <!-- Order Info Note -->
      <div class="mt-12 text-center bg-white dark:bg-slate-800 p-8 rounded-3xl border border-slate-200 dark:border-slate-700 max-w-3xl mx-auto shadow-sm">
        <h4 class="text-lg font-bold text-slate-900 dark:text-white mb-2">Menerima Pesanan Partai Besar & Event</h4>
        <p class="text-sm text-slate-600 dark:text-slate-300 mb-4">
          Dapatkan harga khusus grosir / reseller untuk acara arisan, ulang tahun, syukuran, dan event kantor.
        </p>
        <a 
          href="https://wa.me/6282166525525?text=Halo%20Donat%20Kentang%20Syifa,%20saya%20ingin%20memesan%20donat" 
          target="_blank"
          class="inline-flex items-center space-x-2 px-6 py-3 rounded-xl bg-emerald-600 hover:bg-emerald-700 text-white font-bold text-sm shadow-md transition-colors"
        >
          <svg class="w-5 h-5 fill-white" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
            <path d="M.057 24l1.687-6.163c-1.041-1.804-1.588-3.849-1.587-5.946.003-6.556 5.338-11.891 11.893-11.891 3.181.001 6.167 1.24 8.413 3.488 2.245 2.248 3.481 5.236 3.48 8.414-.003 6.557-5.338 11.892-11.893 11.892-1.99-.001-3.951-.5-5.688-1.448l-6.705 1.754zm6.597-3.807c1.676.995 3.276 1.591 5.392 1.592 5.448 0 9.886-4.434 9.889-9.885.002-5.462-4.415-9.89-9.881-9.892-5.452 0-9.887 4.434-9.889 9.884-.001 2.225.651 3.891 1.746 5.634l-.999 3.648 3.742-.981zm11.387-5.464c-.074-.124-.272-.198-.57-.347-.297-.149-1.758-.868-2.031-.967-.272-.099-.47-.149-.669.149-.198.297-.768.967-.941 1.165-.173.198-.347.223-.644.074-.297-.149-1.255-.462-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.297-.347.446-.521.151-.172.2-.296.3-.495.099-.198.05-.372-.025-.521-.075-.148-.669-1.611-.916-2.206-.242-.579-.487-.501-.669-.51l-.57-.01c-.198 0-.52.074-.792.372s-1.04 1.016-1.04 2.479 1.065 2.876 1.213 3.074c.149.198 2.095 3.2 5.076 4.487.709.306 1.263.489 1.694.626.712.226 1.36.194 1.872.118.571-.085 1.758-.719 2.006-1.413.248-.695.248-1.29.173-1.414z"/>
          </svg>
          <span>Pesan via WhatsApp DKS</span>
        </a>
      </div>

    </div>

    <!-- Order Modal -->
    <transition name="fade">
      <div v-if="showOrderModal" class="fixed inset-0 z-50 flex items-center justify-center p-4 bg-slate-900/60 backdrop-blur-sm" @click.self="showOrderModal = false">
        <div class="bg-white dark:bg-slate-800 rounded-3xl p-6 sm:p-8 max-w-sm w-full shadow-2xl relative transform transition-all">
          <button @click="showOrderModal = false" class="absolute top-4 right-4 p-2 rounded-full text-slate-400 hover:text-slate-600 hover:bg-slate-100 dark:hover:bg-slate-700 dark:hover:text-slate-200 transition-colors">
            <X class="w-5 h-5" />
          </button>
          
          <div class="text-center mb-6">
            <h3 class="text-xl font-bold text-slate-900 dark:text-white mb-1">Pilih Platform</h3>
            <p class="text-sm text-slate-500 dark:text-slate-400">Pesan <strong class="text-amber-600 dark:text-amber-400">{{ selectedOrderProduct?.name }}</strong> melalui aplikasi berikut:</p>
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
  </section>
</template>

<script setup>
import { ref, computed, onMounted, onUnmounted } from 'vue'
import { UtensilsCrossed, ChevronDown, X, Search } from 'lucide-vue-next'
import ProductCard from './ProductCard.vue'

const activeCategory = ref('Semua')
const searchQuery = ref('')
const showAll = ref(false)
const showOrderModal = ref(false)
const selectedOrderProduct = ref(null)
const categories = ['Semua', 'Klasik', 'Premium', 'Spesial']

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

let animationFrameId
const updateFloating = () => {
  const time = Date.now() / 1500
  floatX.value = Math.sin(time) * 15
  floatY.value = Math.cos(time * 0.8) * 15
  animationFrameId = requestAnimationFrame(updateFloating)
}

onMounted(() => {
  updateFloating()
})

onUnmounted(() => {
  if (animationFrameId) cancelAnimationFrame(animationFrameId)
})

const products = [
  { id: 1, name: 'Strawberry', category: 'Klasik', tag: 'Favorit', icon: '🍓', image: '/images/donuts/donut_strawberry_1784959470202.png', description: 'Glaze strawberry manis dan segar.' },
  { id: 2, name: 'Coklat Kacang', category: 'Klasik', tag: 'Best Seller', icon: '🥜', image: '/images/donuts/donut_coklat_kacang_1784959483573.png', description: 'Cokelat premium bertabur kacang panggang.' },
  { id: 3, name: 'Vanilla Kacang', category: 'Klasik', tag: '', icon: '🥜', image: '/images/donuts/donut_vanilla_kacang_1784959965286.png', description: 'Glaze vanilla dengan taburan kacang renyah.' },
  { id: 4, name: 'Coklat Meises', category: 'Klasik', tag: 'Favorit', icon: '🍫', image: '/images/donuts/donut_coklat_meises_1784959975557.png', description: 'Cokelat tebal dengan taburan meises klasik.' },
  { id: 5, name: 'Vanilla Kopi', category: 'Klasik', tag: '', icon: '☕', image: '/images/donuts/donut_vanilla_kopi_1784959985986.png', description: 'Glaze vanilla dipadu dengan aroma kopi.' },
  { id: 6, name: 'Greentea', category: 'Premium', tag: 'Baru', icon: '🍵', image: '/images/donuts/donut_greentea_1784959492966.png', description: 'Matcha greentea lumer dengan paduan white chocolate.' },
  { id: 7, name: 'Crumble Matcha', category: 'Premium', tag: '', icon: '🍵', image: '/images/donuts/donut_crumble_matcha.jpg', description: 'Glaze matcha dengan remahan biskuit renyah.' },
  { id: 8, name: 'Coklat Keju', category: 'Premium', tag: 'Best Seller', icon: '🧀', image: '/images/donuts/donut_coklat_keju.jpg', description: 'Perpaduan cokelat lumer dan parutan keju gurih.' },
  { id: 9, name: 'Blueberry', category: 'Klasik', tag: '', icon: '🫐', image: '/images/donuts/donut_blueberry.jpg', description: 'Glaze blueberry manis yang lembut di mulut.' },
  { id: 10, name: 'Taro Oreo', category: 'Premium', tag: 'Favorit', icon: '🍩', image: '/images/donuts/donut_taro_oreo_1784959505338.png', description: 'Taro creamy berpadu dengan remahan oreo.' },
  { id: 11, name: 'Crumble Oreo', category: 'Premium', tag: '', icon: '🍪', image: '/images/donuts/donut_crumble_oreo.jpg', description: 'Glaze vanilla berselimut remahan oreo pekat.' },
  { id: 12, name: 'Vanilla Keju', category: 'Klasik', tag: 'Baru', icon: '🧀', image: '/images/donuts/donut_vanilla_keju_1784959526343.png', description: 'Glaze vanilla dengan keju cheddar melimpah.' },
  { id: 13, name: 'Redvelvet', category: 'Premium', tag: '', icon: '🍩', image: '/images/donuts/donut_redvelvet.jpg', description: 'Glaze red velvet kaya rasa dengan krim keju.' },
  { id: 14, name: 'Caramel', category: 'Klasik', tag: '', icon: '🍬', image: '/images/donuts/donut_caramel.jpg', description: 'Karamel manis gurih dengan tekstur memikat.' },
  { id: 15, name: 'Vanilla Oreo', category: 'Premium', tag: '', icon: '🍪', image: '/images/donuts/donut_vanilla_oreo.jpg', description: 'Glaze vanilla dengan topping kepingan oreo.' },
  { id: 16, name: 'Coklat Dark', category: 'Klasik', tag: '', icon: '🍫', image: '/images/donuts/donut_coklat_dark.jpg', description: 'Cokelat hitam pekat premium yang lezat.' },
  { id: 17, name: 'Crumble Redvelvet', category: 'Premium', tag: '', icon: '🍩', image: '/images/donuts/donut_crumble_redvelvet.jpg', description: 'Red velvet dengan remahan biskuit spesial.' },
  { id: 18, name: 'Bombo Coklat', category: 'Spesial', tag: 'Best Seller', icon: '🍩', image: '/images/donuts/donut_bombo_coklat_1784959516241.png', description: 'Bomboloni isi krim cokelat lumer yang nikmat.' },
  { id: 19, name: 'Bombo Strawberry', category: 'Spesial', tag: '', icon: '🍓', image: '/images/donuts/donut_bombo_strawberry.jpg', description: 'Bomboloni dengan isian selai strawberry segar.' },
  { id: 20, name: 'Bombo Blueberry', category: 'Spesial', tag: '', icon: '🫐', image: '/images/donuts/donut_bombo_blueberry.jpg', description: 'Bomboloni dengan isian selai blueberry manis.' },
  { id: 21, name: 'Coklat Kelapa', category: 'Klasik', tag: '', icon: '🥥', image: '/images/donuts/donut_coklat_kelapa.jpg', description: 'Cokelat lumer bertabur kelapa parut kering.' },
  { id: 22, name: 'Mocha', category: 'Klasik', tag: '', icon: '☕', image: '/images/donuts/donut_mocha.jpg', description: 'Glaze moka dengan aroma kopi dan cokelat.' },
  { id: 23, name: 'Coklat Oreo', category: 'Premium', tag: '', icon: '🍪', image: '/images/donuts/donut_coklat_oreo.jpg', description: 'Cokelat premium dengan kepingan oreo.' },
  { id: 24, name: 'Avocado', category: 'Premium', tag: '', icon: '🥑', image: '/images/donuts/donut_avocado.jpg', description: 'Glaze alpukat creamy yang segar dan lezat.' }
]

const filteredProducts = computed(() => {
  let result = products
  
  if (activeCategory.value !== 'Semua') {
    result = result.filter(p => p.category === activeCategory.value)
  }
  
  if (searchQuery.value.trim()) {
    const query = searchQuery.value.toLowerCase().trim()
    result = result.filter(p => p.name.toLowerCase().includes(query))
  }
  
  return result
})

const displayedProducts = computed(() => {
  if (showAll.value) return filteredProducts.value
  return filteredProducts.value.slice(0, 9)
})

const handleOrder = (product) => {
  selectedOrderProduct.value = product
  showOrderModal.value = true
}
</script>

<style scoped>
@keyframes gradient-bg {
  0% { background-position: 0% 50%; }
  50% { background-position: 100% 50%; }
  100% { background-position: 0% 50%; }
}
.animate-gradient-bg {
  background-size: 200% 200%;
  animation: gradient-bg 15s ease infinite;
}
</style>
