from action import models
from django.db import transaction
def actionResponse(count,stu_num,tkid,concertid):

    curconcert = models.Concert.objects.get(pk=concertid)
    curtk=models.Ticket.objects.get(pk=tkid)

    flag=True
    try:
        with transaction.atomic():
            for each_stu in stu_num:
                oldfan=models.Fan.objects.filter(cardid=each_stu).first()
                newaccount = int(oldfan.account) - int(curtk.price)
                res1=models.Fan.objects.filter(cardid=each_stu).update(is_select=1,account=newaccount)
                record=models.FanTicket(fan=oldfan,ticket=curtk)
                record.save()

            newremain_tk=int(curtk.remain)-int(count)
            res3=models.Ticket.objects.filter(pk=tkid).update(remain=newremain_tk)

            newremain_seat=int(curconcert.remain_seat)-int(count)
            res4=models.Concert.objects.filter(pk=concertid).update(remain_seat=newremain_seat)

    except Exception as e:
        flag=False
    if(flag):
        return "购票成功"
    return "购票失败，请刷新重试"



