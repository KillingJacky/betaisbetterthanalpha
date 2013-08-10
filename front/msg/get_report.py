#coding: utf-8

__all__ = ['get_report', 'report_not_found']


def get_report(value):
    return u'现在的环境温度：%r  湿度: %s  '
    '固体颗粒物浓度： %s  甲醛气体浓度： %s' % (value['t'], value['h'],
                                                value['pm'], value['ch'])


def report_not_found():
    return u'暂时没有报告哦'
