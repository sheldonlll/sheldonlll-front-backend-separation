<template>
  <v-app class="grey lighten-5 app">
<!-- 	  <VueDragResize :w="200" :h="100" :x="200" :y="0" v-on:resizing="resize" v-on:dragging="resize" class="box">
		<div class="bar">Hello</div>
		<div class="down">
			<div class="left">
				left
			</div>
			<div class="right">
				right
			</div>
		</div>
	  </VueDragResize>
 -->	
	<Navbar></Navbar>
    <v-main>
		<router-view v-if="isRouterAlive"></router-view>
    </v-main>
	<ScrollTop></ScrollTop>
	<Footer></Footer>
  </v-app>
</template>

<script>
	import Navbar from '@/components/Navbar.vue'
	import Footer from '@/components/Footer.vue'
	import ScrollTop from '@/components/ScrollTop.vue'
    import VueDragResize from 'vue-drag-resize';
	export default {
		name: 'App',
		components:{
			Navbar,
			Footer,
			ScrollTop,
			VueDragResize
		},
		data () {
		      return {
		        isRouterAlive: true,
				vw: 0,
				vh: 0,
				top: 0,
				left:0
		      }
		},
		created() {
		　　this.vw = 200 + "px";
		　　this.vh = 200 + "px";
		},
		provide(){ //提供
		  return {
			reload: this.reload
		  }
		},
		methods: {
		  reload(){
			this.isRouterAlive = false
			this.$nextTick( function () {
			  this.isRouterAlive = true
			})
		  },
		  resize(newRect) {
		  	this.vw = newRect.width;
		  	this.vh = newRect.height;
		  	this.top = newRect.top;
		  	this.left = newRect.left;
		  },
		}
	}
</script>
<style scoped="scoped">
	.box{
		background-color: #CCCCCC;
		
	}
	.bar{
		height:20px;
		background-color: #CC9393;
	}
	.down{
		height: 100%;
		display: flex;
		flex-direction: row;
	}
	.left{
		width: 20%;
		background-color: green;
	}
	.right{
		height: 100%;
		background-color: #1290BF;
		width: 80%;
	}
</style>

