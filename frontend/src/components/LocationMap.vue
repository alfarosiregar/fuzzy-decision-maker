<template>
  <section id="lokasi" class="relative py-20 lg:py-28 overflow-hidden bg-slate-50 dark:bg-slate-900/60 transition-colors duration-300">
    <!-- Background Decor Accents -->
    <div class="absolute top-1/2 right-0 -translate-y-1/2 w-[500px] h-[500px] bg-amber-500/10 rounded-full blur-3xl -z-10 pointer-events-none"></div>
    <div class="absolute bottom-0 left-10 w-72 h-72 bg-orange-500/10 rounded-full blur-2xl -z-10 pointer-events-none"></div>

    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      
      <!-- Section Header -->
      <div class="text-center max-w-3xl mx-auto space-y-4 mb-12">
        <div class="inline-flex items-center space-x-2 px-4 py-2 rounded-full bg-amber-100 dark:bg-amber-950/60 border border-amber-300/50 dark:border-amber-700/50 text-amber-800 dark:text-amber-300 text-xs sm:text-sm font-semibold shadow-sm">
          <MapPin class="w-4 h-4 text-amber-600 dark:text-amber-400 animate-bounce" />
          <span>Lokasi Outlet Kami</span>
        </div>
        
        <h2 class="text-3xl sm:text-4xl lg:text-5xl font-extrabold text-slate-900 dark:text-white tracking-tight">
          Kunjungi Outlet <span class="text-gradient">DKS</span>
        </h2>
        
        <p class="text-base sm:text-lg text-slate-600 dark:text-slate-300 leading-relaxed">
          Nikmati kelezatan donat kentang hangat yang dibuat fresh setiap hari. Temukan rute tercepat dan kunjungi lokasi toko cabang kami yang terdekat dari Anda.
        </p>
      </div>

      <!-- Branch Selector Dropdown -->
      <div class="flex justify-center mb-10">
        <div class="relative w-full max-w-md">
          <select 
            v-model="selectedBranchIndex" 
            class="block w-full appearance-none bg-white dark:bg-slate-800 border-2 border-slate-200 dark:border-slate-700 hover:border-amber-400 dark:hover:border-amber-500 text-slate-700 dark:text-slate-200 py-3.5 px-5 pr-10 rounded-2xl leading-tight focus:outline-none focus:ring-4 focus:ring-amber-500/20 focus:border-amber-500 transition-all duration-300 font-semibold cursor-pointer shadow-sm"
          >
            <optgroup label="Area Medan & Sekitarnya">
              <template v-for="(branch, index) in branches" :key="'medan_'+index">
                <option v-if="branch.area === 'Area Medan & Sekitarnya'" :value="index">
                  📍 {{ branch.name }}
                </option>
              </template>
            </optgroup>
            
            <optgroup label="Luar Kota Medan / Wilayah Lain di Sumut">
              <template v-for="(branch, index) in branches" :key="'luar_'+index">
                <option v-if="branch.area === 'Luar Kota Medan / Wilayah Lain di Sumut'" :value="index">
                  📍 {{ branch.name }}
                </option>
              </template>
            </optgroup>
          </select>
          <div class="pointer-events-none absolute inset-y-0 right-0 flex items-center px-4 text-slate-500 dark:text-slate-400">
            <svg class="fill-current h-5 w-5" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20"><path d="M9.293 12.95l.707.707L15.657 8l-1.414-1.414L10 10.828 5.757 6.586 4.343 8z"/></svg>
          </div>
        </div>
      </div>

      <!-- Main Content Grid -->
      <div class="grid lg:grid-cols-12 gap-8 items-center">
        
        <!-- Left Store Info Cards -->
        <div class="lg:col-span-5 space-y-6">
          
          <!-- Card 1: Store Address -->
          <div class="group p-6 rounded-3xl bg-white dark:bg-slate-800 border border-slate-200/80 dark:border-slate-700/80 shadow-xl shadow-slate-200/50 dark:shadow-none hover:border-amber-500/50 transition-all duration-300">
            <div class="flex items-start space-x-4">
              <div class="w-12 h-12 rounded-2xl bg-gradient-to-tr from-amber-600 to-amber-500 flex items-center justify-center text-white shadow-lg shadow-amber-500/30 group-hover:scale-110 transition-transform duration-300 shrink-0">
                <Store class="w-6 h-6" />
              </div>
              <div class="space-y-1">
                <h3 class="text-lg font-bold text-slate-900 dark:text-white">Alamat Outlet</h3>
                <p class="text-sm font-semibold text-slate-800 dark:text-slate-200 leading-relaxed">
                  {{ currentBranch.address }}
                </p>
              </div>
            </div>
          </div>

          <!-- Card 2: Operating Hours -->
          <div class="group p-6 rounded-3xl bg-white dark:bg-slate-800 border border-slate-200/80 dark:border-slate-700/80 shadow-xl shadow-slate-200/50 dark:shadow-none hover:border-amber-500/50 transition-all duration-300">
            <div class="flex items-start space-x-4">
              <div class="w-12 h-12 rounded-2xl bg-gradient-to-tr from-orange-600 to-amber-500 flex items-center justify-center text-white shadow-lg shadow-orange-500/30 group-hover:scale-110 transition-transform duration-300 shrink-0">
                <Clock class="w-6 h-6" />
              </div>
              <div class="space-y-1">
                <h3 class="text-lg font-bold text-slate-900 dark:text-white">Jam Operasional Toko</h3>
                <div class="space-y-1">
                  <p class="text-sm font-bold text-slate-800 dark:text-slate-200">
                    Buka Setiap Hari (Senin - Minggu)
                  </p>
                  <p :class="['text-sm font-semibold flex items-center space-x-2.5', isOpen ? 'text-emerald-600 dark:text-emerald-400' : 'text-rose-600 dark:text-rose-400']">
                    <span class="relative flex h-2.5 w-2.5 shrink-0">
                      <span :class="['animate-ping absolute inline-flex h-full w-full rounded-full opacity-75 [animation-duration:3s]', isOpen ? 'bg-emerald-400' : 'bg-rose-400']"></span>
                      <span :class="['relative inline-flex rounded-full h-2.5 w-2.5', isOpen ? 'bg-emerald-500' : 'bg-rose-500']"></span>
                    </span>
                    <span>{{ isOpen ? 'Buka' : 'Tutup' }} {{ currentBranch.hours }}</span>
                  </p>
                </div>
              </div>
            </div>
          </div>

          <!-- Card 3: Contact & Order -->
          <div class="group p-6 rounded-3xl bg-white dark:bg-slate-800 border border-slate-200/80 dark:border-slate-700/80 shadow-xl shadow-slate-200/50 dark:shadow-none hover:border-amber-500/50 transition-all duration-300">
            <div class="flex items-start space-x-4">
              <div class="w-12 h-12 rounded-2xl bg-gradient-to-tr from-emerald-600 to-emerald-500 flex items-center justify-center text-white shadow-lg shadow-emerald-500/30 group-hover:scale-110 transition-transform duration-300 shrink-0">
                <Phone class="w-6 h-6" />
              </div>
              <div class="space-y-1">
                <h3 class="text-lg font-bold text-slate-900 dark:text-white">Layanan Pelanggan</h3>
                <p class="text-sm text-slate-600 dark:text-slate-300">
                  Telepon / WA: <a :href="`https://wa.me/62${currentBranch.phone.replace(/[^0-9]/g, '').substring(1)}`" target="_blank" class="font-bold text-amber-600 dark:text-amber-400 hover:underline">{{ currentBranch.phone }}</a>
                </p>
                <p class="text-xs text-slate-500 dark:text-slate-400">
                  Terima pesanan donat untuk arisan, ulang tahun, & katering.
                </p>
              </div>
            </div>
          </div>

          <!-- Action Buttons -->
          <div class="pt-2 flex flex-col sm:flex-row gap-4">
            <a 
              :href="currentBranch.mapDirectUrl" 
              target="_blank" 
              rel="noopener noreferrer"
              class="w-full inline-flex items-center justify-center space-x-3 px-8 py-4 rounded-2xl bg-gradient-to-r from-amber-600 to-amber-500 hover:from-amber-700 hover:to-amber-600 text-white font-bold text-base shadow-xl shadow-amber-600/30 hover:shadow-amber-600/50 hover:-translate-y-1 transition-all duration-300"
            >
              <Navigation class="w-5 h-5" />
              <span>Buka Google Maps</span>
            </a>
          </div>

        </div>

        <!-- Right Embedded Google Maps Container -->
        <div class="lg:col-span-7">
          <div class="relative rounded-3xl overflow-hidden border-2 border-amber-500/30 dark:border-amber-500/20 shadow-2xl shadow-amber-500/10 group">
            
            <!-- Embedded Google Map Iframe -->
            <div class="w-full h-[450px] lg:h-[550px] bg-slate-200 dark:bg-slate-800 relative transition-opacity duration-300">
              <iframe 
                :key="selectedBranchIndex"
                :title="`Lokasi Donat Kentang Syifa ${currentBranch.name}`"
                :src="currentBranch.mapEmbedUrl"
                class="w-full h-full border-0 filter contrast-[1.05] brightness-[0.98] dark:contrast-[1.1] dark:invert-[0.9] dark:hue-rotate-180"
                allowfullscreen="" 
                loading="lazy" 
                referrerpolicy="no-referrer-when-downgrade"
              ></iframe>
            </div>

            <!-- Overlay Clickable Card on Bottom Right -->
            <div class="absolute bottom-4 right-4 left-4 sm:left-auto z-10">
              <a 
                :href="currentBranch.mapDirectUrl" 
                target="_blank" 
                rel="noopener noreferrer"
                class="inline-flex items-center space-x-2 px-5 py-3 rounded-2xl bg-slate-900/90 hover:bg-slate-900 text-white backdrop-blur-md text-xs font-bold shadow-xl border border-slate-700/80 transition-all hover:scale-105"
              >
                <Compass class="w-4 h-4 text-amber-400" />
                <span>Petunjuk Rute Google Maps</span>
                <ExternalLink class="w-3.5 h-3.5" />
              </a>
            </div>

          </div>
        </div>

      </div>

    </div>
  </section>
</template>

<script setup>
import { ref, computed } from 'vue'
import { MapPin, Store, Clock, Phone, Navigation, ExternalLink, Compass } from 'lucide-vue-next'

const branches = [
  // Area Medan & Sekitarnya
  {
    area: "Area Medan & Sekitarnya",
    name: "Jl. Setia Budi (Tanjung Rejo)",
    address: "Jl. Setia Budi No.75, Tj. Rejo, Kec. Medan Sunggal, Kota Medan, Sumatera Utara",
    hours: "09:00 - 21:00 WIB",
    phone: "0821-6652-5525",
    mapEmbedUrl: "https://maps.google.com/maps?q=Jl.+Setia+Budi+No.75,+Tj.+Rejo,+Medan+Sunggal,+Sumatera+Utara&t=&z=16&ie=UTF8&iwloc=&output=embed",
    mapDirectUrl: "https://www.google.com/maps/search/Donat+Kentang+Syifa+Setia+Budi+Medan/"
  },
  {
    area: "Area Medan & Sekitarnya",
    name: "Jl. Sei Musi (Babura Sunggal)",
    address: "Jl. Sei Musi, Babura Sunggal, Kec. Medan Sunggal, Kota Medan, Sumatera Utara",
    hours: "09:00 - 21:00 WIB",
    phone: "0821-6652-5525",
    mapEmbedUrl: "https://maps.google.com/maps?q=Jl.+Sei+Musi,+Babura+Sunggal,+Medan+Sunggal,+Sumatera+Utara&t=&z=16&ie=UTF8&iwloc=&output=embed",
    mapDirectUrl: "https://www.google.com/maps/search/Donat+Kentang+Syifa+Sei+Musi+Medan/"
  },
  {
    area: "Area Medan & Sekitarnya",
    name: "Terjun (Medan Marelan)",
    address: "Terjun, Kec. Medan Marelan, Kota Medan, Sumatera Utara",
    hours: "09:00 - 21:00 WIB",
    phone: "0821-6652-5525",
    mapEmbedUrl: "https://maps.google.com/maps?q=Donat+Kentang+Syifa+Terjun+Medan+Marelan+Sumatera+Utara&t=&z=16&ie=UTF8&iwloc=&output=embed",
    mapDirectUrl: "https://www.google.com/maps/search/Donat+Kentang+Syifa+Terjun+Medan+Marelan/"
  },
  {
    area: "Area Medan & Sekitarnya",
    name: "Jl. Tuasan (Sidorejo Hilir)",
    address: "Jl. Tuasan, Sidorejo Hilir, Kec. Medan Tembung, Kota Medan, Sumatera Utara",
    hours: "09:00 - 21:00 WIB",
    phone: "0821-6652-5525",
    mapEmbedUrl: "https://maps.google.com/maps?q=Jl.+Tuasan,+Sidorejo+Hilir,+Medan+Tembung,+Sumatera+Utara&t=&z=16&ie=UTF8&iwloc=&output=embed",
    mapDirectUrl: "https://www.google.com/maps/search/Donat+Kentang+Syifa+Tuasan+Medan+Tembung/"
  },
  {
    area: "Area Medan & Sekitarnya",
    name: "Jl. Karya Wisata (Medan Johor)",
    address: "Jl. Karya Wisata, Gedung Johor, Kec. Medan Johor, Kota Medan, Sumatera Utara (Tersedia via GoFood)",
    hours: "09:00 - 21:00 WIB",
    phone: "0821-6652-5525",
    mapEmbedUrl: "https://maps.google.com/maps?q=Jl.+Karya+Wisata,+Gedung+Johor,+Medan+Johor,+Sumatera+Utara&t=&z=16&ie=UTF8&iwloc=&output=embed",
    mapDirectUrl: "https://www.google.com/maps/search/Donat+Kentang+Syifa+Karya+Wisata+Medan+Johor/"
  },
  
  // Luar Kota Medan / Wilayah Lain di Sumut
  {
    area: "Luar Kota Medan / Wilayah Lain di Sumut",
    name: "Jl. Perintis Kemerdekaan (Binjai)",
    address: "Jl. Perintis Kemerdekaan, Kota Binjai, Sumatera Utara",
    hours: "09:00 - 21:00 WIB",
    phone: "0821-6652-5525",
    mapEmbedUrl: "https://maps.google.com/maps?q=Donat+Kentang+Syifa+Jl.+Perintis+Kemerdekaan,+Binjai,+Sumatera+Utara&t=&z=16&ie=UTF8&iwloc=&output=embed",
    mapDirectUrl: "https://www.google.com/maps/search/Donat+Kentang+Syifa+Perintis+Kemerdekaan+Binjai/"
  },
  {
    area: "Luar Kota Medan / Wilayah Lain di Sumut",
    name: "Jl. DR. Sutomo (Lubuk Pakam)",
    address: "Jl. DR. Sutomo, Lubuk Pakam, Kab. Deli Serdang, Sumatera Utara",
    hours: "09:00 - 21:00 WIB",
    phone: "0821-6652-5525",
    mapEmbedUrl: "https://maps.google.com/maps?q=Donat+Kentang+Syifa+Jl.+DR.+Sutomo,+Lubuk+Pakam,+Deli+Serdang,+Sumatera+Utara&t=&z=16&ie=UTF8&iwloc=&output=embed",
    mapDirectUrl: "https://www.google.com/maps/search/Donat+Kentang+Syifa+Lubuk+Pakam+Deli+Serdang/"
  },
  {
    area: "Luar Kota Medan / Wilayah Lain di Sumut",
    name: "Jl. Veteran (Tebing Tinggi)",
    address: "Jl. Veteran, Kota Tebing Tinggi, Sumatera Utara",
    hours: "09:00 - 21:00 WIB",
    phone: "0821-6652-5525",
    mapEmbedUrl: "https://maps.google.com/maps?q=Donat+Kentang+Syifa+Jl.+Veteran,+Tebing+Tinggi,+Sumatera+Utara&t=&z=16&ie=UTF8&iwloc=&output=embed",
    mapDirectUrl: "https://www.google.com/maps/search/Donat+Kentang+Syifa+Veteran+Tebing+Tinggi/"
  },
  {
    area: "Luar Kota Medan / Wilayah Lain di Sumut",
    name: "Jl. Imam Bonjol (Kisaran)",
    address: "Jl. Imam Bonjol, Kisaran, Kab. Asahan, Sumatera Utara",
    hours: "09:00 - 21:00 WIB",
    phone: "0821-6652-5525",
    mapEmbedUrl: "https://maps.google.com/maps?q=Donat+Kentang+Syifa+Jl.+Imam+Bonjol,+Kisaran,+Asahan,+Sumatera+Utara&t=&z=16&ie=UTF8&iwloc=&output=embed",
    mapDirectUrl: "https://www.google.com/maps/search/Donat+Kentang+Syifa+Imam+Bonjol+Kisaran+Asahan/"
  },
  {
    area: "Luar Kota Medan / Wilayah Lain di Sumut",
    name: "Sitamiang (Padangsidimpuan)",
    address: "Sitamiang, Kota Padangsidimpuan, Sumatera Utara",
    hours: "09:00 - 21:00 WIB",
    phone: "0821-6652-5525",
    mapEmbedUrl: "https://maps.google.com/maps?q=Donat+Kentang+Syifa+Sitamiang,+Padangsidimpuan,+Sumatera+Utara&t=&z=16&ie=UTF8&iwloc=&output=embed",
    mapDirectUrl: "https://www.google.com/maps/search/Donat+Kentang+Syifa+Sitamiang+Padangsidimpuan/"
  },
  {
    area: "Luar Kota Medan / Wilayah Lain di Sumut",
    name: "Jln. Gereja (Pematang Siantar)",
    address: "Jln. Gereja (Berseberangan dengan Irian Supermarket), Kota Pematang Siantar, Sumatera Utara",
    hours: "09:00 - 21:00 WIB",
    phone: "0821-6652-5525",
    mapEmbedUrl: "https://maps.google.com/maps?q=Donat+Kentang+Syifa+Jln.+Gereja,+Pematang+Siantar,+Sumatera+Utara&t=&z=16&ie=UTF8&iwloc=&output=embed",
    mapDirectUrl: "https://www.google.com/maps/search/Donat+Kentang+Syifa+Jln.+Gereja+Pematang+Siantar/"
  }
]

const selectedBranchIndex = ref(0)

const currentBranch = computed(() => branches[selectedBranchIndex.value])

// Compute if store is open based on WIB time (UTC+7)
const isOpen = computed(() => {
  const now = new Date()
  const utc = now.getTime() + (now.getTimezoneOffset() * 60000)
  const wibTime = new Date(utc + (3600000 * 7))
  const hour = wibTime.getHours()
  // Store is open from 09:00 to 21:00
  return hour >= 9 && hour < 21
})
</script>
