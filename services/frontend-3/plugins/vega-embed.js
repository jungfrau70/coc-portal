import {default as vegaEmbed} from 'vega-embed'
  
export default {
  methods: {
    reloadImage () {
      fetch('/vega-example').then(response => {
        response.json().then(spec => {
          vegaEmbed('#vega-box', spec, {actions: false})
        })
      })
    }
  }
}