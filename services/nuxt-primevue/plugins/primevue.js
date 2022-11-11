import PrimeVue from 'primevue/config'
import Button from 'primevue/button'
import InputText from 'primevue/inputtext'
import Toast from 'primevue/toast'
import ToastService from 'primevue/toastservice'

export default defineNuxtPlugin(nuxtApp => {
    nuxtApp.vueApp.use(PrimeVue, { ripple: true })
    nuxtApp.vueApp.use(ToastService)
    nuxtApp.vueApp.component('Button', Button)
    nuxtApp.vueApp.component('InputText', InputText)
    nuxtApp.vueApp.component('Toast', Toast)
    //other components that you need
})

// import { defineNuxtPlugin } from "#app";
// import PrimeVue from "primevue/config";
// import Button from "primevue/button";
// import InputText from 'primevue/inputtext';
// import Toast from 'primevue/toast';
// import ToastService from 'primevue/toastservice';

// import DataTable from 'primevue/datatable';
// import Column from 'primevue/column';
// import ColumnGroup from 'primevue/columngroup';     //optional for column grouping
// import Row from 'primevue/row';                     //optional for row

// export default defineNuxtPlugin(nuxtApp => {
//     nuxtApp.vueApp.use(PrimeVue, { ripple: true })
//     nuxtApp.vueApp.use(ToastService)
//     nuxtApp.vueApp.component('Button', Button)
//     nuxtApp.vueApp.component('InputText', InputText)
//     nuxtApp.vueApp.component('Toast', Toast)
//     nuxtApp.vueApp.component('ToastService', ToastService)
//     //other components that you need    
//     nuxtApp.vueApp.component('DataTable', DataTable)
//     nuxtApp.vueApp.component('Column', Column)
//     nuxtApp.vueApp.component('ColumnGroup', ColumnGroup)
//     nuxtApp.vueApp.component('Row', Row)

// })

