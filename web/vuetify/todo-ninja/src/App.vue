<template>
  <v-app>
    <!-- <v-toolbar app dark height="60" class="indigo">  
      <v-toolbar-title class="headline text-uppercase">
        <span>뷰티파이 연습</span>
        <span class="font-weight-light">메터리얼 디자인</span>
      </v-toolbar-title>
      <v-spacer></v-spacer>
      <v-btn
        flat
        href="https://github.com/vuetifyjs/vuetify/releases/latest"
        target="_blank"
      >
        <span class="mr-2">최신 릴리즈</span>
      </v-btn>
    </v-toolbar> -->

    <v-content >
      <!-- <HelloWorld/> -->
      <router-view></router-view>
    </v-content>
  </v-app>
</template>

<script>
// import HelloWorld from './components/HelloWorld'

export default {
  name: 'App',
  // components: {
  //   HelloWorld
  // },
  data () {
    return {
      //
    }
  }
}
</script>
