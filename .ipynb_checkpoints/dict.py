{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "65473285",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter a language: 안녕하세요\n"
     ]
    },
    {
     "ename": "AttributeError",
     "evalue": "'NoneType' object has no attribute 'group'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mAttributeError\u001b[0m                            Traceback (most recent call last)",
      "\u001b[1;32m~\\AppData\\Local\\Temp/ipykernel_3052/4068925285.py\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m      7\u001b[0m \u001b[1;31m# detected = translator.detect(sentence)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      8\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 9\u001b[1;33m \u001b[0mprint\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mtranslator\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mdetect\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0msentence\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[1;32m~\\anaconda3\\lib\\site-packages\\googletrans\\client.py\u001b[0m in \u001b[0;36mdetect\u001b[1;34m(self, text, **kwargs)\u001b[0m\n\u001b[0;32m    253\u001b[0m             \u001b[1;32mreturn\u001b[0m \u001b[0mresult\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    254\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 255\u001b[1;33m         \u001b[0mdata\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m_translate\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mtext\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;34m'en'\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;34m'auto'\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mkwargs\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    256\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    257\u001b[0m         \u001b[1;31m# actual source language that will be recognized by Google Translator when the\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\anaconda3\\lib\\site-packages\\googletrans\\client.py\u001b[0m in \u001b[0;36m_translate\u001b[1;34m(self, text, dest, src, override)\u001b[0m\n\u001b[0;32m     76\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     77\u001b[0m     \u001b[1;32mdef\u001b[0m \u001b[0m_translate\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mself\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mtext\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mdest\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0msrc\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0moverride\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m---> 78\u001b[1;33m         \u001b[0mtoken\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mtoken_acquirer\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mdo\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mtext\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m     79\u001b[0m         params = utils.build_params(query=text, src=src, dest=dest,\n\u001b[0;32m     80\u001b[0m                                     token=token, override=override)\n",
      "\u001b[1;32m~\\anaconda3\\lib\\site-packages\\googletrans\\gtoken.py\u001b[0m in \u001b[0;36mdo\u001b[1;34m(self, text)\u001b[0m\n\u001b[0;32m    192\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    193\u001b[0m     \u001b[1;32mdef\u001b[0m \u001b[0mdo\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mself\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mtext\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 194\u001b[1;33m         \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m_update\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    195\u001b[0m         \u001b[0mtk\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0macquire\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mtext\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    196\u001b[0m         \u001b[1;32mreturn\u001b[0m \u001b[0mtk\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\anaconda3\\lib\\site-packages\\googletrans\\gtoken.py\u001b[0m in \u001b[0;36m_update\u001b[1;34m(self)\u001b[0m\n\u001b[0;32m     60\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     61\u001b[0m         \u001b[1;31m# this will be the same as python code after stripping out a reserved word 'var'\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m---> 62\u001b[1;33m         \u001b[0mcode\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mRE_TKK\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0msearch\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mr\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mtext\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mgroup\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;36m1\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mreplace\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m'var '\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;34m''\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m     63\u001b[0m         \u001b[1;31m# unescape special ascii characters such like a \\x3d(=)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     64\u001b[0m         \u001b[0mcode\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mcode\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mencode\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mdecode\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m'unicode-escape'\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mAttributeError\u001b[0m: 'NoneType' object has no attribute 'group'"
     ]
    }
   ],
   "source": [
    "from googletrans import Translator\n",
    "\n",
    "translator = Translator()\n",
    "\n",
    "sentence = input(\"Enter a language: \")\n",
    "dest = input(\"What language do you want to translate it with\")\n",
    "\n",
    "# detected = translator.detect(sentence)\n",
    "result = translator.translate(sentence, dest)\n",
    "defected = translator.detect(sentence)\n",
    "\n",
    "\n",
    "print(detected.lang, \":\", sentence)\n",
    "print(result.dest, \":\", result.text)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "bab6c727",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
