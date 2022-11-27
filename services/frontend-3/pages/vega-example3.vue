<template>
  <div>
    <section>
      Index
      <header>
        <button @click="prev">previous</button>
        <select v-model="current" @change="fromDrop">
          <option v-for="item in list" :key="item">{{ item }}</option>
        </select>
        <button @click="next">next</button>
      </header>

      <div class="hor">
        <div id="viz"></div>
        <div class="edit">
          <textarea v-model="def"></textarea>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
import embed from 'vega-embed'

const BASEURL = 'https://vega.github.io/vega-lite/'

export default {
  data() {
    return {
      current: null,
      def: null,
      index: 0,
      list: ['airport_connections.vl.json', 'area.vl.json'],
    }
  },
  watch: {
    def(v) {
      if (v) this.draw()
    },
  },
  methods: {
    prev() {
      this.index--
      this.current = this.list[this.index]
      this.load()
    },
    next() {
      this.index++
      this.current = this.list[this.index]
      this.load()
    },
    fromDrop() {
      this.index = this.list.indexOf(this.current)
      this.load()
    },
    async load() {
      const src = await this.$axios(`${BASEURL}examples/${this.current}`)
      const ob = src.data
      if (ob.data.url) {
        ob.data.url = BASEURL + ob.data.url
      }
      this.def = JSON.stringify(ob, true, 2)
    },
    async draw() {
      const struct = JSON.parse(this.def)
      struct.width = 'container'
      struct.height = 'container'
      await embed('#viz', struct, { actions: false })
    },
  },
}
</script>
