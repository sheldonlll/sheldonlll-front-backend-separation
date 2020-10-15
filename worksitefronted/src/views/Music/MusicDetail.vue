<template>
	<v-container>
	    <v-row>
			<v-col>
				<h1>MusicDetail</h1>
			</v-col>
		</v-row>
	</v-container>
</template>

<script>
	export default{
		name:'BlogDetail',
		data(){
			return{
				
			}
		},
		created() {
			console.log(this.$route.params.id)
		}
	}
</script>

<style scoped="scoped">
</style>
