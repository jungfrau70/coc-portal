<template>
  <div>
    <b-navbar toggleable="lg" type="dark" variant="info">
      <b-navbar-brand href="#">HOME</b-navbar-brand>

      <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

      <b-collapse id="nav-collapse" is-nav>
        <b-navbar-nav>
          <b-dropdown size="lg" text="작업관리" class="m-2">
            <NuxtLink to="/incident" class="navbar-item">인시던트</NuxtLink>
            <NuxtLink to="/issue" class="navbar-item"> 이슈 </NuxtLink>
            <NuxtLink to="/problem" class="navbar-item"> 문제 </NuxtLink>
            <NuxtLink to="/change" class="navbar-item"> 변경 </NuxtLink>
            <NuxtLink to="/request" class="navbar-item"> 요청 </NuxtLink>
          </b-dropdown>
          <b-dropdown size="lg" text="자산관리" class="m-2">
            <NuxtLink to="/instance" class="navbar-item">인스턴스(VM)</NuxtLink>
            <NuxtLink to="/database" class="navbar-item">데이터베이스</NuxtLink>
            <NuxtLink to="/kubernetes" class="navbar-item">쿠버네티스</NuxtLink>
          </b-dropdown>
          <b-dropdown size="lg" text="예방관리" class="m-2">
            <NuxtLink to="/incident" class="navbar-item">인시던트</NuxtLink>
            <NuxtLink to="/issue" class="navbar-item"> 이슈 </NuxtLink>
            <NuxtLink to="/problem" class="navbar-item"> 문제 </NuxtLink>
            <NuxtLink to="/change" class="navbar-item"> 변경 </NuxtLink>
            <NuxtLink to="/request" class="navbar-item"> 요청 </NuxtLink>
          </b-dropdown>
        </b-navbar-nav>

        <!-- Right aligned nav items -->
        <b-navbar-nav class="ml-auto">
          <b-nav-form>
            <b-form-input
              size="sm"
              class="mr-sm-2"
              placeholder="Search"
            ></b-form-input>
            <b-button size="sm" class="my-2 my-sm-0" type="submit"
              >Search</b-button
            >
          </b-nav-form>
        </b-navbar-nav>

        <b-navbar-nav v-if="!auth">
          <NuxtLink to="/login" class="navbar-item">Login</NuxtLink>
          <NuxtLink to="/register" class="navbar-item">Register</NuxtLink>                   
        </b-navbar-nav>
        <b-navbar-nav v-if="auth">
          <NuxtLink to="/logout" class="navbar-item">Logout</NuxtLink>     
        </b-navbar-nav>
      </b-collapse>
    </b-navbar>
    <main class="form-signin">
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

<style>
.form-signin {
  width: 100%;
  max-width: 330px;
  padding: 15px;
  margin: auto;
}

.form-signin .checkbox {
  font-weight: 400;
}

.form-signin .form-control {
  position: relative;
  box-sizing: border-box;
  height: auto;
  padding: 10px;
  font-size: 16px;
}

.form-signin .form-control:focus {
  z-index: 2;
}

.form-signin input[type="username"] {
  margin-bottom: -1px;
  border-bottom-right-radius: 0;
  border-bottom-left-radius: 0;
}

.form-signin input[type="password"] {
  margin-bottom: 10px;
  border-top-left-radius: 0;
  border-top-right-radius: 0;
}
</style>

