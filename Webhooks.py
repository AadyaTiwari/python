noWebhooksPGs = {'loantap', 'payglocal', 'hdfc', 'paytm_upi', 'mpgs', 'twid', 'capitalfloat', 'paypal', 'sbi', 'freecharge', 'mobikwik', 'zaakpay', 'simpl', 'cybersource', 'migs', 'airtelmoney', 'amex', 'cash', 'citrus', 'dummy', 'ebs', 'ebs_v3', 'epaylater', 'fsspay', 'ipg', 'jiomoney', 'lazypay', 'olamoney', 'olapostpaid', 'sodexo', 'icicinb'}

def generateUrl(mid, PG):
    
    sandbox = f"https://sandbox.juspay.in/v2/pay/webhooks/{mid}/{PG}"
    prod = f"https://api.juspay.in/v2/pay/webhooks/{mid}/{PG}"

    print("Webhook URLs are: ")
    print('sandbox URL: ', sandbox)
    print('prod URL: ', prod)

    if PG == 'amazonpay':
        appName = input("Enter app name: ")
        packageName = input("Enter package name: ")
        bundle = input("Enter iOS bundle ID: ")
        env = ["sandbox", 'prod']
        print(f"amzn://amazonpay.amazon.in/{mid}")
        print(f"Amzn-{packageName}")
        print(packageName)
        print(f"amzn-{bundle}://pwa")
        print(f"{packageName}://customtab.juspay.in/{packageName}")


        for i in env:
            print(f"https://{i}.juspay.in/pay/sdk-response/apps/{packageName}?app_name={appName}")
            print(f"https://{i}.juspay.in/pay/response-amazonpay/{mid}")
            print(f"https://{i}.juspay.in/v2/pay/response-amazonpay/{mid}")
            print(f"https://{i}.juspay.in/v3/pay/response-amazonpay/{mid}")
            print(f"https://{i}.juspay.in/v2/wallets/topup-response/AMAZONPAY/{mid}")
            print(f"https://{i}.juspay.in/v3/wallets/topup-response/AMAZONPAY/{mid}")

        
if __name__ == "__main__":
    flag = True
    PG = input("Enter PG: ")
    PG = PG.lower()
    if PG in noWebhooksPGs: 
        print(f"{PG.upper()} doesn't support webhooks!")
        flag = False
    if flag:    
        mid = input("Enter MID: ")
        generateUrl(mid, PG)

# from tkinter import * 
# from tkinter import ttk

# tcl = Tcl()
# print(tcl.call("info", "patchlevel"))

# root = Tk()

# frm = ttk.Frame(root, padding=10)
# frm.grid()
# ttk.Label(frm, text="Enter PG").grid(column=0, row=0)
# ttk.Label(frm, text = "Enter MID").grid(column = 0, row = 1)
# ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
# root.mainloop()
