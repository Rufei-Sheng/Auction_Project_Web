var baseUrl = 'http://127.0.0.1:8000/';

var APIURL = {
    //	register
    register :"index/register/",
//    login
    login: "index/login/",
//   post profuct
    publish: "index/publish/",

//    get product list
    get_product_list:"index/get_product_list/",
//    whether liked
    get_prise: "index/get_prise/",
//    add liked and cancel
    add_prise: "index/add_prise/",
//    auction product

    add_buy: "index/add_buy/",

//    get the purchased history
    get_auction_list: "index/get_auction_list/",
//    update user information
    up_user_info: "index/up_user_info/",
//    dis-regist 
    del_user_info: "index/del_user_info/",

//   get liked product
    get_liked: "index/get_liked/",

//   end winner
    update_end_success: "index/update_end_success/",

    get_post_list:"index/get_post_list/"

}


/*
 *ajax
 * @url:request path
 * @method:request method
 * @params:parameters
 * @callback:callback
 * @iswait
 * @waitword
 * */
function apiAjax(url,method,params,callback){
    $.ajax({
        url: baseUrl + url,
        type: method,
        ContentType: "application/json",
        dataType: "json",
        async: false,
        processData: true,
        timeout: 20,
        data: params,
        success: function(ret) {
            console.log("success")
            console.log(ret)
            if(ret.code == 1){
                callback(ret);
            }else{
                alert(ret.err_msg);
            }
        },
        error: function(err) {
            console.log("error")
            console.log(err)
        }
    })
}

