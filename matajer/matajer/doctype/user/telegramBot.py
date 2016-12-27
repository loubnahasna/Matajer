from __future__ import unicode_literals
import frappe
from frappe import _
import telepot

@frappe.whitelist(allow_guest= True)
def send_message(doc,method):
    bot = telepot.Bot('329789734:AAETIeAP4ibpR5XPZKZSD-i9y1cdEYjiwVg')
    bot.sendMessage(-138408095, 'A new product has just been added !!!!!')
    frappe.msgprint(_("Hooks are working !!"))
