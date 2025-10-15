from pyscript import document, alert, window

def calculate(event):
    q1=to_int(document.getElementById('q1').value)
    q2=to_int(document.getElementById('q2').value)
    q3=to_int(document.getElementById('q3').value)
    p1=150
    p2=95
    p3=120
    subtotal=q1*p1+q2*p2+q3*p3
    fee=round(subtotal*0.10,2)
    tax=round(subtotal*0.12,2)
    total=round(subtotal+fee+tax,2)
    summary=f"Customer: {document.getElementById('cname').value}\nContact: {document.getElementById('cphone').value}\n\nItems:\n Signature Sandwich x{q1} @ {p1}\n Truffle Fries x{q2} @ {p2}\n Maison Latte x{q3} @ {p3}\n\nSubtotal: ₱{subtotal}\nService Fee (10%): ₱{fee}\nTax (12%): ₱{tax}\nTotal: ₱{total}\nPickup: {document.getElementById('ptime').value}\nNotes: {document.getElementById('notes').value}"
    document.getElementById('summary').innerText=summary

def placeOrder(event):
    calculate()
    alert('Order placed successfully!')

def clearForm(event):
    document.getElementById('orderForm').reset()
    document.getElementById('summary').innerText=''

def sendContact(event):
    name=document.getElementById('conname').value
    document.getElementById('cresp').innerText=f'Thanks, {name}. Your message has been received.'

window.sendContact = sendContact
window.calculate = calculate
window.placeOrder = placeOrder
window.clearForm = clearForm