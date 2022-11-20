Refs
- https://v3.nuxtjs.org/getting-started/installation/
- https://github.com/NimzyMaina/nuxtDt

#############################################################################################
# 1. Project 
#############################################################################################

npx nuxi init nuxt-primevue
cd nuxt-primevue

or
npx create-nuxt-app nuxt-front

#############################################################################################
# 2. plugin (module) 설치
#############################################################################################

yarn add primevue primeicons primeflex


#############################################################################################
# 3. app 에 plugin (module) 추가
#    ==> 즉, plugins 폴더에 javascript 파일 추가
#############################################################################################

cat << EOF > plugins\primevue.js
import { defineNuxtPlugin } from "#app";
import PrimeVue from "primevue/config";
import Button from "primevue/button";
import InputText from 'primevue/inputtext';
import Toast from 'primevue/toast';
import ToastService from 'primevue/toastservice';

export default defineNuxtPlugin(nuxtApp => {
    nuxtApp.vueApp.use(PrimeVue, { ripple: true })
    nuxtApp.vueApp.use(ToastService)
    nuxtApp.vueApp.component('Button', Button)
    nuxtApp.vueApp.component('InputText', InputText)
    nuxtApp.vueApp.component('Toast', Toast)
    //other components that you need
})


#############################################################################################
# 4. server-side 에 plugin 추가
#    ==> 즉, nuxt.config.js 파일 plugins 에 javascript 파일 추가
#############################################################################################

// Plugins to run before rendering page: https://go.nuxtjs.dev/config-plugins

cat << EOF > nuxt.config.ts
export default defineNuxtConfig({
	css: [
		'primevue/resources/themes/saga-blue/theme.css',
		'primevue/resources/primevue.css',
		'primeicons/primeicons.css',
		'primeflex/primeflex.css'
	],
	build: {
		transpile: ['primevue']
	}
})

#############################################################################################
# 4. server-side 에 css 추가
#    ==> 즉, nuxt.config.js 파일 css 에 css 파일 추가
#############################################################################################

  // Global CSS: https://go.nuxtjs.dev/config-css
  css: [
    "~/static/css/style.css",
    "~/static/css/bootstrap.min.css",
    "~/static/css/datatables.min.css",
  ],


#############################################################################################
# 5. start coding
#############################################################################################

yarn install
yarn dev

