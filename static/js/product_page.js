var product_page = new Vue({
    el: '#product_page',
    data: {
      product_list:null,
    },
    create(){
        this.get_product_list()
    },
    methods:{
        get_product_list:function(){
            axios.get('/product_list/')
            .then(res => {
                console.log(res)
                this.product_list=res.data
            })
            .catch(err => {
                console.error(err); 
            })
        },
        
    }
  })