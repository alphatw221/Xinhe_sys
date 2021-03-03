var worksheet = new Vue({
    el: '#update_use_product_sheet',
    data: {
      use_product_sheet:null,
      isFetching:true,
      products:[],
    },
    created(){
        this.isFetching=true
        const url = window.location.href
        const parts=url.split('/')
        axios.get('/use_product_sheet_detail/'+parts[parts.length-1])
        .then(res => {
            console.log(res.data)
            this.use_product_sheet=res.data.use_product_sheet
            this.products=res.data.products
            this.isFetching=false
        }).catch(err => { console.error(err); })
    },
    methods:{
        add_products(){
            this.products.push({product:null,code:null,name:"--",unit:'--',warehouse:this.use_product_sheet.warehouse,date:this.use_product_sheet.date,use_product_sheet:this.use_product_sheet.id})
        },
        submit(){
            data=[]
            for(i=0;i<this.products.length;i++){
                data.push({product:this.products[i].product,
                    amount:this.products[i].amount,
                    warehouse:this.use_product_sheet.warehouse,
                    date:this.use_product_sheet.date,
                    use_product_sheet:this.use_product_sheet.id,
                    })
            }
            axios.put('/use_product_sheet_detail/'+this.use_product_sheet.id,{use_product_sheet:this.use_product_sheet,use_product_sheet_productss:data})
            .then(res => {
                window.alert(res.data['message'])
                location.reload()
            })
            .catch(err => {
                window.alert('更新資料錯誤')
            })
            
        },
        search_product(index){
            axios.get('/get_product_with_code/',{params:{code:this.products[index].code}})
                .then(res => {
                    this.products[index].name=res.data.name
                    this.products[index].unit=res.data.unit
                    this.products[index].product=res.data.id
                })
        },
        cancel_product(index){
            this.products.splice(index,1)
        }
    }
})