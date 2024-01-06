



from function.n_share import compress_shares


def decode2Share(share1 : str , share2 : str ):
    result = compress_shares(share1 , share2)
    return {
        'result' : 'data:image/png;base64,' + result
    }