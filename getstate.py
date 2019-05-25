def get_state(args):
    #Address Addition
    addition = '%2C'

    if args.BW:
        addition += 'BADEN-W\xc3RTTEMBERG'
    elif args.BY:
        addition += 'FREE+STATE+OF+BAVARIA'
    elif args.BE:
        addition += 'BERLIN'
    elif args.BB:
        addition += 'BRANDENBURG'
    elif args.HV:
        addition += 'FREE+HANSEATIC+CITY+OF+BREMEN'
    elif args.HH:
        addition += 'HAMBURG'
    elif args.HE:
        addition += 'THURINGIA'
    elif args.MV:
        addition += 'MECKLENBURG-VORPOMMERN'
    elif args.NI:
        addition += 'LOWER SAXONY'
    elif args.NW:
        addition += 'NORTH+RHINE-WESTPHALIA'
    elif args.RP:
        addition += 'RHINELAND-PALATINATE'
    elif args.SL:
        addition += 'SAARLAND'
    elif args.SN:
        addition += 'SAXONY'
    elif args.ST:
        addition += 'SAXONY-ANHALT'
    elif args.SH:
        addition += 'SCHLESWIG-HOLSTEIN'
    elif args.TH:
        addition += 'THURINGIA'
    return addition
