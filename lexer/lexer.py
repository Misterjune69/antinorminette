import dict
import re

#if __name__ == "__main__":
#	raise Exception("This is a lexical analizer module, you idiot. IT'S A M-O-D-U-L-E.")

tokens = []

def lexer_mod (src):
	lex = {
		"linenbr": 0,
		"tabs": 0
	}
	str = ""
	for i, v in enumerate(dict.__all__):
		for ia, va in enumerate(v):
			print(v[va])
			match = re.match(src, va)
			if (match != -1):
				tokens.append({
					"token": v[va],
					"value": va,
					"pos": (lex.linenbr, match + lex.tabs * 4)
				})
				if (v[va] == "NEW_LINE"):
					lex.linenbr += 1
					lex.tabs = 0
					elif (v[va] == "TAB"):
					lex.tabs += 1
				break

lexer_mod("Hello!")

__all__ = [tokens]
