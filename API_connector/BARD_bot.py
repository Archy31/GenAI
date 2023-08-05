from bardapi import Bard, BardCookies
from pprint import pprint

BARD_API = "ZQi3X9se3ufVZLtBRgTWnPbFT6-G1oFVYfT9WOFg0pyv0LHP3wdN7s91rCzkd16RPKhiRA."

cookie_dict = {
    "__Secure-1PSID": "ZQi3X9se3ufVZLtBRgTWnPbFT6-G1oFVYfT9WOFg0pyv0LHP3wdN7s91rCzkd16RPKhiRA.",
    "__Secure-1PSIDTS": "sidts-CjEBSAxbGSPmO494sYtblsV-fzO-TFOasbBbWcUD_6Fx5nhf4CsHGu8BCaH2yqC_OzCLEAA",
}

message = input("Give me text >>>  ")


while message:
    bard = BardCookies(cookie_dict=cookie_dict)

    pprint(bard.get_answer(message)["content"])
    
    message = input("Give me text >>>  ")