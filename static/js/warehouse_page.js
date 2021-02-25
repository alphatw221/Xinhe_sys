var worksheet = new Vue({
    el: '#warehouse_dashboard',
    data: {
        n:0,
        squad:null,
        warehouses:null,
        warehouse:null,
        paginate_select:20,
        products:[],
        dict:null,
        products_inout:{},
    },
    created(){
        axios.get('/get_all_dict/')
            .then(res => {
                this.dict=res.data
                console.log(this.dict)
            }).catch(err => { console.error(err);   })
    },
    methods:{
        update_warehouse(){
            this.warehouses=null
            axios.get('/get_squad_warehouses/'+this.squad)
            .then(res => {
                this.warehouses=res.data
                
            })
            
        },
        add_product(){
            this.products.push({id:null,code:null,name:'料名:--',unit:'單位:--'})
        },
        cancel_product(index){
            this.products.splice(index,1)
        },
        search_product(index){
            axios.get('/get_product_with_code/',{params:{code:this.products[index].code}})
                .then(res => {
                    this.products[index].name='料名:'+res.data.name
                    this.products[index].unit='單位:'+res.data.unit
                    this.products[index].id=res.data.id
                })
        },
        search(){
            products_id=[]
            for(i=0;i<this.products.length;i++){
                products_id.push(this.products[i].id)
            }
            console.log(products_id)
            axios.post('/get_warehouse_inout/'+this.warehouse,{ids:products_id})
                .then(res => {
                    this.products_inout=res.data
                    console.log(this.products_inout)
                })
        },

    },
    
})