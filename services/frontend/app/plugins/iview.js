import Vue from "vue";
import iView from "view-design";
import 'view-design/dist/styles/iview.css';
import locale from "view-design/dist/locale/en-US"; // Change locale, check node_modules/iview/dist/locale

export default () => {
  Vue.use(iView, {
    locale
  });
}