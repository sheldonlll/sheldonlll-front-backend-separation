<template>
	<v-card flat>
		<v-toolbar dense flat @click="ishow">
			<span>弹幕列表</span>
			<v-btn icon>
			  <v-icon>mdi-dots-vertical</v-icon>
			</v-btn>
			<v-spacer></v-spacer>
			<v-btn depressed v-show="show">展开</v-btn>
			<v-btn depressed v-show="!show">收起</v-btn>
		</v-toolbar>
	  </v-card>
</template>

<script>
	export default{
		data(){
			return{
				show:false
			}
		},
		methods:{
			ishow(){
				this.show = !this.show
			}
		},
		props:{
			ObjectId:{
				type:Number,
				default:0
			},
			ContentType:{
				type:Number,
				default:0
			}
		}
	}
</script>

<style>
</style>
