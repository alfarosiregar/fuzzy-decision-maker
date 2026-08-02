<template>
  <div class="bg-white dark:bg-slate-900 rounded-3xl overflow-hidden shadow-sm hover:shadow-xl transition-all duration-300 border border-slate-100 dark:border-slate-800 flex flex-col group">
    <!-- Image Header / Badge Container -->
    <div class="relative h-48 bg-gradient-to-br from-amber-100 to-amber-50 dark:from-slate-800 dark:to-slate-900 flex items-center justify-center overflow-hidden">
      <!-- Product Image -->
      <img 
        v-if="product.image" 
        :src="product.image" 
        :alt="product.name"
        class="w-full h-full object-cover transition-transform duration-700 group-hover:scale-110"
      />
      <!-- Fallback Donut Emoji Avatar with Glow -->
      <div v-else class="text-7xl group-hover:scale-110 transition-transform duration-300 select-none filter drop-shadow-md">
        {{ product.icon }}
      </div>
      
      <!-- Tag Badge -->
      <div v-if="product.tag" class="absolute top-4 right-4 px-3 py-1 rounded-full text-xs font-bold shadow-sm" :class="tagClass">
        {{ product.tag }}
      </div>

      <div class="absolute bottom-3 left-4 flex items-center space-x-1 text-amber-500 text-xs font-bold bg-white/90 dark:bg-slate-800/90 px-2.5 py-1 rounded-lg backdrop-blur-sm">
        <Star class="w-3.5 h-3.5 fill-amber-400 text-amber-400" />
        <span>{{ product.rating }}</span>
      </div>
    </div>

    <!-- Product Details -->
    <div class="p-6 flex-1 flex flex-col justify-between space-y-4">
      <div class="space-y-2">
        <div class="flex items-center justify-between">
          <span class="text-xs font-bold uppercase tracking-wider text-amber-600 dark:text-amber-400">
            {{ product.category }}
          </span>
          <span class="text-xs text-slate-500 dark:text-slate-400">
             Isi {{ product.packSize }}
          </span>
        </div>
        
        <h3 class="text-xl font-bold text-slate-900 dark:text-white group-hover:text-amber-600 dark:group-hover:text-amber-400 transition-colors">
          {{ product.name }}
        </h3>
        
        <p class="text-xs sm:text-sm text-slate-600 dark:text-slate-400 leading-relaxed line-clamp-2">
          {{ product.description }}
        </p>
      </div>

      <!-- Price & Order Action -->
      <div class="pt-4 border-t border-slate-100 dark:border-slate-800 flex items-center justify-between">
        <div>
          <span class="text-xs text-slate-400 block mb-1">Harga</span>
          <div class="flex flex-col space-y-0.5">
            <span class="text-sm sm:text-base font-extrabold text-slate-900 dark:text-white leading-none">
              Rp 3.000 <span class="text-[10px] font-normal text-slate-500">/ Pc</span>
            </span>
            <span class="text-sm sm:text-base font-extrabold text-slate-900 dark:text-white leading-none">
              Rp 18.000 <span class="text-[10px] font-normal text-slate-500">/ Kotak</span>
            </span>
          </div>
        </div>

        <button 
          @click="onOrder" 
          class="px-4 py-2.5 rounded-xl bg-amber-100 dark:bg-slate-800 hover:bg-amber-600 hover:text-white dark:hover:bg-amber-500 text-amber-800 dark:text-amber-300 font-bold text-xs sm:text-sm transition-all duration-300 flex items-center space-x-1.5"
        >
          <ShoppingCart class="w-4 h-4" />
          <span>Pesan</span>
        </button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { computed } from 'vue'
import { Star, ShoppingCart } from 'lucide-vue-next'

const props = defineProps({
  product: {
    type: Object,
    required: true
  }
})

const emit = defineEmits(['order'])

const tagClass = computed(() => {
  if (props.product.tag === 'Best Seller') return 'bg-amber-500 text-white'
  if (props.product.tag === 'Favorit') return 'bg-rose-500 text-white'
  if (props.product.tag === 'Baru') return 'bg-emerald-500 text-white'
  return 'bg-slate-700 text-white'
})

const onOrder = () => {
  emit('order', props.product)
}
</script>
