<template v-for="(chart, index) in charts" :key="index">
  <div id="vis"></div>
</template>
  

<script>
import embed from 'vega-embed'
// import worldMap from '@highcharts/map-collection/custom/world.geo.json'
import data from '../data/penguins.json'

export default {
  data() {
    return {
      name: 'myData',
      // values: data,
      charts: [
      {
        $schema: 'https://vega.github.io/schema/vega-lite/v5.json',
        // $schema: 'https://vega.github.io/schema/vega-lite/v2.0.json',
        description: 'A simple bar chart with embedded data.',
        data: {
          values: data
        },
        mark: 'bar',
        encoding: {
          x: { field: 'a', type: 'nominal', axis: { labelAngle: 0 } },
          y: { field: 'b', type: 'quantitative' },
        },
      },
      {
        $schema: 'https://vega.github.io/schema/vega-lite/v5.json',
        // $schema: 'https://vega.github.io/schema/vega-lite/v2.0.json',
        description: 'A simple bar chart with embedded data.',
        data: {
          values: [
            { a: 'A', b: 28 },
            { a: 'B', b: 55 },
            { a: 'C', b: 43 },
            { a: 'D', b: 91 },
            { a: 'E', b: 81 },
            { a: 'F', b: 53 },
            { a: 'G', b: 19 },
            { a: 'H', b: 87 },
            { a: 'I', b: 52 },
          ],
        },
        mark: 'bar',
        encoding: {
          x: { field: 'a', type: 'nominal', axis: { labelAngle: 0 } },
          y: { field: 'b', type: 'quantitative' },
        },
      },
      ]
      

    }
  },

  mounted() {
    this.draw()
    console.log(process.env.API_URL)
  },
  methods: {
    async draw() {
      const result = await embed('#vis', this.charts[1])
      // const result = await embed('#vis', this.hconcat)
      return result
    },
  },
}
</script>
