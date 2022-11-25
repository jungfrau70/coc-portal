<template>
  <v-card>
    <v-toolbar color="cyan" dark flat>
      <v-app-bar-nav-icon></v-app-bar-nav-icon>

      <v-toolbar-title>Lenz Dashboard</v-toolbar-title>

      <v-spacer></v-spacer>

      <v-btn icon>
        <v-icon>mdi-magnify</v-icon>
      </v-btn>

      <v-btn icon>
        <v-icon>mdi-dots-vertical</v-icon>
      </v-btn>

      <template v-slot:extension>
        <v-tabs
          icons-and-text
          centered
          show-arrows
          color="white"
          slider-color="pink"
        >
          <v-tab v-for="(i, index) in tabs" :key="index" :href="i.path">
            {{ i.name }}
            <v-icon>{{ i.icon }}</v-icon>
          </v-tab>
        </v-tabs>
      </template>
    </v-toolbar>

    <!-- <v-tabs-items v-model="tab">
      <v-tab-item v-for="(item, index) in items" :key="index">
        <NuxtLink to="/problemlist">장애관리</NuxtLink>
        <v-card flat>
          <v-card-text v-text="text"></v-card-text>
        </v-card>
      </v-tab-item>
    </v-tabs-items> -->
  </v-card>
</template>

<script>
export default {
  data() {
    return {
      tabs: [
        { name: 'Dashboard', icon: 'list', path: '/problemlist' },
        { name: 'Live Location', icon: 'playlist_add', path: '/problemlist' }
      ]
    //   tab: null,
    //   items: [
    //     '인시던트',
    //     '변경관리',
    //     '요청관리',
    //     '보안관리',
    //     '이슈관리',
    //     '문제관리',
    //     '자산관리[DB]',
    //     '자산관리[K8s]',
    //     '자산관리[Instance]',
    //     '용량관리',
    //     '백업관리',
    //     '정기점검',
    //   ],
    //   text: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
    }
  },
}
</script>
