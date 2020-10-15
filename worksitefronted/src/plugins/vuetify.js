import 'material-design-icons-iconfont/dist/material-design-icons.css' // Ensure you are using css-loader
import Vue from 'vue'
import Vuetify from 'vuetify/lib'

Vue.use(Vuetify)

export default new Vuetify({
  icons: {
    iconfont: 'md',
  },
  theme: {
      themes: {
        light: {
          primary: '#29B6F6',
          secondary: '#3cd1c2',
          accent: '#C0CA33',
          error: '#f83e70',
        },
      },
    },
})