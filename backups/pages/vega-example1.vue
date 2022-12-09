<template>
  <div id="viz2"></div>
</template>

<script>
import embed from "vega-embed";

export default {
  name: "ScatterFacet",
  async mounted() {
    const def = {
      $schema: "https://vega.github.io/schema/vega/v5.json",
      description: "The Trellis display",
      background: "white",
      padding: 5,
      data: [
        {
          name: "source_0",
          url: "tsne_bert_base_cased_sentiment_multi.csv",
          format: { type: "dsv", delimiter: "," },
          transform: [
            {
              type: "filter",
              expr: "datum.epoch == epoch",
            },
          ],
        },
      ],
      signals: [
        { name: "tsne_child_width", value: 200 },
        { name: "tsne_y_step", value: 200 },
        {
          name: "tsne_child_height",
          update: "bandspace(domain('tsne_y').length, 10, 0) * tsne_y_step",
        },
        {
          name: "epoch",
          value: 0,
          bind: { input: "range", min: 0, max: 3, step: 1 },
        },
      ],
      layout: { padding: 5, bounds: "full", align: "all", columns: 4 },
      marks: [
        {
          name: "tsne_cell",
          type: "group",
          title: {
            text: {
              signal:
                'isValid(parent["layer"]) ? "layer "+parent["layer"] : ""+parent["layer"]',
            },
            style: "guide-label",
          },
          style: "cell",
          from: {
            facet: {
              name: "tsne_facet",
              data: "source_0",
              groupby: ["layer"],
            },
          },
          encode: {
            update: {
              width: { signal: "tsne_child_width" },
              height: { signal: "tsne_child_height" },
            },
          },
          marks: [
            {
              type: "symbol",
              style: ["point"],
              from: { data: "tsne_facet" },
              encode: {
                update: {
                  stroke: { scale: "label_color", field: "label" },
                  x: { scale: "tsne_x", field: "x" },
                  y: { scale: "tsne_y", field: "y" },
                },
              },
            },
          ],
        },
      ],
      spec: {
        selection: {
          slider: {
            type: "single",
            fields: ["epoch"],
            bind: {
              epoch: { input: "range", min: 0, max: 4, step: 1 },
            },
          },
        },
      },
      scales: [
        {
          name: "tsne_x",
          type: "linear",
          domain: { data: "source_0", field: "x" },
          range: [0, { signal: "tsne_child_width" }],
          nice: true,
          zero: true,
        },
        {
          name: "tsne_y",
          type: "linear",
          domain: { data: "source_0", field: "y" },
          range: [0, { signal: "tsne_y_step" }],
          nice: true,
          zero: true,
        },
        {
          name: "label_color",
          type: "ordinal",
          domain: { data: "source_0", field: "label", sort: true },
          range: "category",
        },
        {
          name: "color",
          type: "ordinal",
          domain: { data: "source_0", field: "label", sort: true },
          range: "category",
        },
      ],
      legends: [
        {
          symbolType: "circle",
          title: "Label",
          fill: "color",
          titleFontSize: "16",
          labelFontSize: "12",
        },
      ],
      config: {},
    };
    await embed("#viz2", def, { actions: false });
  },
};
</script>

<style>
</style>
