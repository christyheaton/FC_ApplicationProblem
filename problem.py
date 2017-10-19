# http://www.fogcreek.com/jobs/SupportEngineerLevel1

def text_to_dict(text):
    '''returns a dictionary with characters as keys and their counts as values'''
    d = {}
    for c in text:
        if c in d:
            d[c] += 1
        else:
            d[c] = 1
    return d

def sort_by_count(sorted_by_count, to_sort):
    '''returns a sorted string of the entire to_sort string'''
    init_result = ''
    for i in sorted_by_count:
        if i in to_sort:
            init_result = init_result + i
    return init_result

if __name__ == '__main__':

    text = r'cwrxwzbgickpjbp_svnudntddwdqbfgzyiqpuxddmpvyfquosmicfzkjekxzchngpqaksafulateukuwomdrwza_n_ptzktjzcuibnebe_tqessrzqewgkadrkvtyznaupodanwazopg_fijcoojojbsolr_ejesukzc_quochdnmti_lkvrsegyieqlqysuxdvetkqtkhxaiypfdiddztlicjurnllriopdtuuzpryrsepfydyeg_xkr_ruxp_lgqesysidfsygztwrba_ay_gaqqklbrvr_lbhawjraqujfxptmuvqfzklfodgaqrnhjravksjwemoosdlxtvw_qspxmlvqryusfixzlkb_p_c_tepzozzwnokvqspkizygoqpbhjnsxopchzgapctowbrletrunlgnvzpfwrqgedo_s_ygkxz_mpncnve_gfpbotupawevhfxvqhwlerupjfibosbvhiijrodigzyhy_iijes_xsqorshhdzkjqitpljsftpitjetwmzqiabyiewgtbjaddtsjkckcxxvlyrchloetluxkohn_uihkdjpcqgvejanslakmwendgkmvmayknvjjnr_kdapnumwvz__lsimxdtrflyleykxejl_jbkhexpcyreoapelqzzyriyrbxdgbgwrrxlj_pt_mpwubvbveakxfsbfgj___xfqilxpzalazduzucgoxz_yzhkjwamosiwclkicifmebonobknqokyevtwmekackk_kezmjkgmtgaouerwlwfkaaqhkghreoqhfjzpxrlzmbgfpvofpxkmz_cnvcvfsuokpcaimnvdxeizbbgudln__wvkrqpijlncdacmsvytdxmu_zkvzilfrymoxzlovfhdzuarqumibrcvuqfcxdcrvw_ehbwhwjoanluezhthzkpuqd_efilprbskomczdhdoyudx_sybyfuako_xmorjtdnvwlwskpxnhjhmamiyxbyhh_reqlnkbzmrn_oleixht_v_tigjuxpkmmdpxznvbeqdzuedlfywxmcrbttdp_nfzusrrvpttbtabticgdx_cdiookdmupufqhlwiidaveibsyrviqsyvgledamchipkibjftdedyxzqjgvyyrcgwopo_vmldkrzhlatforljbeeqvgonrradkgmzin_mjbareajhewvyiidczysmrmzppgiifvqecxixbtukignqzr_pzokiedmwsw_usamiqngdiolwahtkbyhob_xpvmkdvqbvywmmtogfjogumfom_ppfut_cnxnjwjeiuidnapodo_wiqvgluofjatvkwowosn_vbmdsrwkhbnmlwctcrb_ycyklnxsbhbjkpknlfsccburlfhjhteqnnwrcfonrqifiapfeqqbv_d_rgddzqkjt_eeinwww_oxropsvcpuignzzudsjugxghobkurukspjygbowcic_rmuaatueajsbdswcwnhjaoujs_nbcmmrfjqoqchrvgehdewpicqanwilpirqghzkklsfczavcegoqdflxqamzsppfozsmrmmrzjlfrbxcljdmvxeaxnifyjluwfnqdzmwzepzzxmbyev_ms_flxgevtmyiqifnrsclobraupspnpndekgyxhlkyhuaahgonahtcmhim_ufoevtvemqffnmpgqmxqatvamwaqvogmdottva__yhjbuvco_wytdxssnbqrlqlvcaltxwfaej_ycvlcdqzwxphhwxitcvrpzcdrmmfancifskzzpltgpyskiqpcqiwsufibt_pvquhqadcllygxcshnbrudltm_pkjyfnolo_wqdwhbwpuvduuodtkfhqqzmvjfhvsfdhyi_fkhuspwvqiaestpgkqelgo_lnmmodlmfmyggpizxbjautpleio_zalvo_ryrymndvnzqyermzsrycngihghtampsdpidttqdmqo_iwieomfruotxfduawlrxsbuoncjmqehmtiyqzbilxloywkmtrbvmg__fxczgkcxecgjobcfenwztzivnfwijcmjlqcqcxdkozmjbmfxxuwlawcinh_lbzmepageirjmszxlwfqiaeisrfnuxpiexsgpjo_hvaojqyzqrkdohewbeipbvbqmefftjixqrnzrufbc_ombxljpmiedfnra_ugpnispsrrsuoeckawzsdfvwlgmwxub_hpccvlbwyyyqcxdcsl_f_vwvsgzptetyyjuemsnpkpcgdlxkuyyljhcquwrivsvuhbwvhf_jtgnvvlqpgufpvlgbtlhfrzxfhxoeolhq_muflllumega'

    to_sort = 'abcdefghijklmnopqrstuvwxyz_'

    # get a dictionary of the text {character:count}
    d = text_to_dict(text)
    # get a list of the dictionary keys sorted by frequency, descending
    sorted_text = sorted(d, key=d.get, reverse=True)
    # sort the to_sort string by the number of times the character appears in the text
    init_result = sort_by_count(sorted_text, to_sort)
    # print everything before the underscore
    print(init_result.split('_')[0])
