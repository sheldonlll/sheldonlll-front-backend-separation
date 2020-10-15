<template>
	<v-container>
		<div class="f">
			<v-btn v-show="gotop" @click="goUp" class="c">
				<v-icon>navigation</v-icon>
			</v-btn>
		</div>
	</v-container>
</template>

<script>
	export default{
		data(){
			return{
				gotop: false
			}
		},
		mounted() {
		    window.addEventListener("scroll", this.handleScroll, true);
		},
		methods:{
			handleScroll(){
				let scrolltop = document.documentElement.scrollTop || document.body.scrollTop;
				scrolltop > 30 ? (this.gotop = true) : (this.gotop = false);
			},
			goUp(){
				let top = document.documentElement.scrollTop || document.body.scrollTop;
				const timeTop = setInterval(() => {
				document.body.scrollTop = document.documentElement.scrollTop = top -= 50;
				if (top <= 0) {
				  clearInterval(timeTop);
				}
			  }, 5);
			}
		}
	}
</script>

<style scoped="scoped">
	.f .c{
	  position: fixed;
	  right: 183px;
	  bottom: 30px;
	  cursor: pointer;
	  padding: 10px;
	}
</style>
