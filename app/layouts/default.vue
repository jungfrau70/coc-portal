<template>
  <div>
    <nav class="navbar" role="navigation" aria-label="main navigation">
      <div class="navbar-brand">
        <a
          class="navbar-item"
          href="https://github.com/jungfrau70/p-lenz-portal.git"
        >
          <img src="/lenz.png" width="31" height="31" />
        </a>

        <a
          role="button"
          class="navbar-burger"
          aria-label="menu"
          aria-expanded="false"
          data-target="navbarBasicExample"
        >
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
        </a>
      </div>

      <div id="navbarBasic" class="navbar-menu">
        <div class="navbar-start">
          <NuxtLink to="/" class="navbar-item"> Home </NuxtLink>
          <NuxtLink to="/current" class="navbar-item"> 운영현황 </NuxtLink>
          <!-- <ul class="navbar-nav me-auto mb-2 mb-md-0" v-if="auth"> -->
          <ul class="navbar-item me-auto mb-2 mb-md-0" v-if="!auth">
            <div class="navbar-item has-dropdown is-hoverable">
              <NuxtLink to="/task" class="navbar-link"> 작업관리 </NuxtLink>

              <div class="navbar-dropdown">
                <NuxtLink to="/incident" class="navbar-item">
                  인시던트
                </NuxtLink>
                <NuxtLink to="/issue" class="navbar-item"> 이슈 </NuxtLink>
                <NuxtLink to="/problem" class="navbar-item"> 문제 </NuxtLink>
                <NuxtLink to="/change" class="navbar-item"> 변경 </NuxtLink>
                <NuxtLink to="/request" class="navbar-item"> 요청 </NuxtLink>
              </div>
            </div>
          </ul>
          <ul class="navbar-item me-auto mb-2 mb-md-0" v-if="!auth">
            <div class="navbar-item has-dropdown is-hoverable">
              <NuxtLink to="/inventory" class="navbar-link">
                자산관리
              </NuxtLink>
              <div class="navbar-dropdown">
                <NuxtLink to="/instance" class="navbar-item">
                  인스턴스(VM)
                </NuxtLink>
                <NuxtLink to="/database" class="navbar-item">
                  데이터베이스
                </NuxtLink>
                <NuxtLink to="/kubernetes" class="navbar-item">
                  쿠버네티스
                </NuxtLink>
              </div>
            </div>
          </ul>
          <ul class="navbar-item me-auto mb-2 mb-md-0" v-if="!auth">
            <div class="navbar-item has-dropdown is-hoverable">
              <NuxtLink to="/preventive" class="navbar-link">
                예방관리
              </NuxtLink>
              <div class="navbar-dropdown">
                <NuxtLink to="/backup" class="navbar-item"> 백업 </NuxtLink>
                <NuxtLink to="/security" class="navbar-item"> 보안 </NuxtLink>
                <NuxtLink to="/regularcheck" class="navbar-item">
                  정기점검
                </NuxtLink>
              </div>
            </div>
          </ul>
        </div>

        <div class="navbar-end">
          <ul class="navbar-nav me-auto mb-2 mb-md-0" v-if="auth">
            <div class="navbar-item">
              <div class="buttons">
                <NuxtLink to="/logout" class="button is-primary" @click="logout"
                  >Logout</NuxtLink
                >
              </div>
            </div>
          </ul>
          <ul class="navbar-nav me-auto mb-2 mb-md-0" v-if="!auth">
            <div class="navbar-item">
              <div class="buttons">
                <NuxtLink to="/preview" class="navbar-brand">Preview</NuxtLink>
                <NuxtLink to="/data" class="navbar-brand">Data</NuxtLink>
                <NuxtLink to="/signup" class="button is-primary"
                  >Signup</NuxtLink
                >
                <NuxtLink to="/login" class="button is-light">Login</NuxtLink>
              </div>
            </div>
          </ul>
        </div>
      </div>
    </nav>

    <main>
      <Nuxt />
    </main>
  </div>
</template>

<script>
export default {
  name: "layout",
  data() {
    return {
      auth: false,
    };
  },
  mounted() {
    this.$nuxt.$on("auth", (auth) => {
      this.auth = auth;
    });
  },
  methods: {
    async signin() {
      await SVGAnimatedEnumeration("http://localhost:8000/account/singup", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        credentials: "include",
      });

      await this.$router.push("/login");
    },
    async login() {
      await fetch("http://localhost:8000/account/login", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        credentials: "include",
      });

      await this.$router.push("/login");
    },
    async logout() {
      await fetch("http://localhost:8000/account/logout", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        credentials: "include",
      });

      await this.$router.push("/login");
    },
  },
};
</script>
