

// env, appname, packagename, mid to be fetched from the logs 
//SDK response URL
function constructAmazonURL(env, appName, packageName){
    return [`https://${env}.juspay.in/pay/sdk-response/apps/${packageName}?app_name=${appName}`,
        `amzn://amazonpay.amazon.in/${mid}`,
        `Amzn-${packageName}`
        `${packageName}`,
        `${packageName}://pwa`,
        `${packageName}://customtab.juspay.in/${packageName}`,
        `https://${env}.juspay.in/pay/response-amazonpay/${mid}`,
        `https://${env}.juspay.in/v2/pay/response-amazonpay/${mid}`,
        `https://${env}.juspay.in/v3/pay/response-amazonpay/${mid}`,
        `https://${env}.juspay.in/v2/wallets/topup-response/AMAZONPAY/${mid}`,
        `https://${env}.juspay.in/v3/wallets/topup-response/AMAZONPAY/${mid}`
    ]
}

