from meteva.base.fun import *
from meteva.product.program.fun import *

def plot(sta_ob_and_fos0,method,s = None,g = None,gll = None,save_dir = None,title = None,para1 = None):

    if s is not None:
        if g is not None:
            if g == "last_range" or g == "last_step":
                s["drop_last"] = False
            else:
                s["drop_last"] = True
    sta_ob_and_fos = sele_by_dict(sta_ob_and_fos0, s)
    #discription_uni = get_unique_coods(sta_ob_and_fos)
    sta_ob_and_fos_list,gll1 = group(sta_ob_and_fos,g,gll)
    data_name = meteva.base.get_stadata_names(sta_ob_and_fos)
    fo_num = len(data_name) -1
    ensemble_score_method = [meteva.method.box_plot_ensemble,meteva.method.rank_histogram]
    group_num = len(sta_ob_and_fos_list)

    valid_gll = []
    if type(method) == str:
        method =  globals().get(method)
    if method in ensemble_score_method:
        for i in range(group_num):
            sta = sta_ob_and_fos_list[i]
            if(len(sta.index) == 0):
                pass
            else:
                valid_group_list = None
                if gll1 is None:
                    valid_gll = None
                else:
                    valid_group_list = gll1[i]
                    valid_gll.append(gll1[i])
                ob = sta[data_name[0]].values
                fo = sta[data_name[1:]].values
                save_path = get_save_path(save_dir,method,g,valid_group_list,"",".png",title)
                #title1 = get_title(method,g,valid_group_list,"",title,discription_uni)

                title1 = meteva.product.program.get_title_from_dict(method, s, g, valid_group_list,
                                                                    None)
                if para1 is None:
                    method(ob, fo,save_path = save_path,title = title1)
                else:
                    method(ob, fo,para1,save_path = save_path,title = title1)
    else:
        for i in range(group_num):
            sta = sta_ob_and_fos_list[i]
            if(len(sta.index) == 0):
                pass
            else:
                valid_group_list = None
                if gll1 is None:
                    valid_gll = None
                else:
                    valid_group_list = gll1[i]
                    valid_gll.append(gll1[i])
                ob = sta[data_name[0]].values

                for j in range(fo_num):
                    fo = sta[data_name[j+1]].values
                    save_path = get_save_path(save_dir,method,g,valid_group_list,data_name[j+1],".png",title)
                    #title1 = get_title(method,g,valid_group_list,data_name[j+1],title,discription_uni)
                    title1 = meteva.product.program.get_title_from_dict(method, s, g, valid_group_list,data_name[j+1])

                    if para1 is None:
                        method(ob, fo,save_path = save_path,title = title1)
                    else:
                        method(ob, fo,para1,save_path = save_path,title = title1)


    return valid_gll
