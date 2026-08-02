import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import path from 'path'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [vue()],
  resolve: {
    alias: {
      '@': path.resolve(__dirname, './src'),
    },
  },
  server: {
    port: 5173,
    host: true,
    allowedHosts: [
      '32bb-36-74-232-168.ngrok-free.app',
      '.ngrok-free.app'
    ],
    proxy: {
      '/app': {
        target: 'http://127.0.0.1:8501',
        changeOrigin: true,
        rewrite: (path) => path.replace(/^\/app/, ''),
        ws: true
      },
      '/static': {
        target: 'http://127.0.0.1:8501',
        changeOrigin: true
      },
      '/_stcore': {
        target: 'http://127.0.0.1:8501',
        changeOrigin: true,
        ws: true
      },
      '/vendor': {
        target: 'http://127.0.0.1:8501',
        changeOrigin: true
      }
    }
  }
})
