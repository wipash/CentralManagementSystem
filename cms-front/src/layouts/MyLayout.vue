<template>
  <q-layout view="lhh lpR lFf">
    <q-header class="bg-primary text-white" elevated>
      <q-toolbar class="bg-primary text-white">
        <q-toolbar-title>Toronto Cat Rescue</q-toolbar-title>
        <q-space></q-space>
        <q-btn flat label="Link" stretch/>
        <q-btn-dropdown flat icon="person" label="" stretch>
          <div class="row no-wrap q-pa-md items-center justify-center" style="width: 200px;">
            <div class="column items-center">
              <q-avatar size="100px">
                <img src="https://cdn.quasar.dev/img/boy-avatar.png">
              </q-avatar>
              <div class="text-subtitle1 q-mt-md q-mb-xs">John Doe</div>
              <q-btn color="primary" label="Logout"/>
            </div>
          </div>
        </q-btn-dropdown>
      </q-toolbar>
    </q-header>

    <q-drawer elevated side="left" v-model="leftDrawer">
      <div class="row q-pa-lg justify-center">
          <q-img src="statics/tcr_logo.png" style="width: 120px;"></q-img>
      </div>
      <q-separator />
      <q-scroll-area class="fit">
        <q-list v-for="(menuItem, index) in menuList" :key="index">

          <q-item clickable :active="true" v-ripple>
            <q-item-section avatar>
              <q-icon :name="menuItem.icon" />
            </q-item-section>
            <q-item-section>
              {{ menuItem.label }}
            </q-item-section>
          </q-item>

          <q-separator v-if="menuItem.separator" />

        </q-list>
      </q-scroll-area>
    </q-drawer>

    <q-page-container>
      <router-view/>
    </q-page-container>

  </q-layout>
</template>

<script lang="ts">
import Vue from 'vue'

const menuList = [
  {
    icon: 'home',
    label: 'Home',
    separator: true
  }
]

export default Vue.extend({
  name: 'MyLayout',
  data () {
    return {
      leftDrawer: true,
      test: true,
      menuList
    }
  }
})
</script>

<style>
</style>
