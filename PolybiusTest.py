from Imports.Ciphers import *
from Utility.Tools import *
import random

def DecodeWithKey(text, key):
    text = StringFormat(text)
    grid = GetPolybiusGrid(key)
    
    coordinates = TextToPolybiusCoordinates(text, grid)
    coordinate_pairs = []
    
    for i in range(len(coordinates) // 2):
        coordinate_pairs.append([coordinates[2 * i], coordinates[2 * i + 1]])
    
    decrypted_coordinate_pairs = []
    
    for coordinate_pair in coordinate_pairs:
        x1, y1 = coordinate_pair[0]
        x2, y2 = coordinate_pair[1]
        
        if (x1, y1) == (x2, y2):
            decrypted_coordinate_pairs.append(coordinate_pair)
            continue
        
        if x1 == x2:
            y1, y2 = (y1 - 1) % 5, (y2 - 1) % 5
        elif y1 == y2:
            x1, x2 = (x1 - 1) % 5, (x2 - 1) % 5
        else:
            y1, y2 = y2, y1
        
        decrypted_coordinate_pairs.append([(x1, y1), (x2, y2)])
    
    decrypted_coordinates = []
    
    for pair in decrypted_coordinate_pairs:
        decrypted_coordinates += pair
            
    text = CoordinatesToText(decrypted_coordinates, grid)
    return text
            
def GetFitness(text):
    text.replace("x", "")
    return SubstitutionFitness(text)

def SwapElements(key):
    key = KeyWithSwaps(key, 1)
    return key

def SwapRow(key):
    to, fro = random.randint(0, 4), random.randint(0, 4)
    grid = GetPolybiusGrid(key)
    temp = grid[fro]
    grid[fro] = grid[to]
    grid[to] = temp
    return GetPolybiusKey(grid)

def SwapColumn(key):
    to, fro = random.randint(0, 4), random.randint(0, 4)
    grid = MakeCosets(key, 5)
    temp = grid[fro]
    grid[fro] = grid[to]
    grid[to] = temp
    return Interleave(grid)

def FlipVertically(key):
    grid = GetPolybiusGrid(key)
    grid.reverse()
    return GetPolybiusKey(grid)

def FlipHorizontally(key):
    grid = MakeCosets(key, 5)
    grid.reverse()
    return Interleave(grid)

def FlipDiagonally(key):
    grid = GetPolybiusGrid(key)
    return Interleave(grid)


def Shift(key):
    key = RotateList(key, random.randint(1, 26))
    return key
    
    
if __name__ == "__main__":
    ciphertext = StringFormat("EGIWLUQ DUOHGKODG, R IK TAWTW RD USERKBD ZER NOIRA, CQU I OIWAHHN: NMIWDGR KR LC QPG OIUICRK. VPG INQ LDR MR HARD IKR XLWLEGF PGCO QMCR WDQS OASI KR HA RLPD OIX DKMGDD YA RCQOUPFUO ORQM IKR LVA IUHWCRD PKRRKGA. M RIKBH IKT SNOO PT LRWDFUDO MF HIWR CQ MKR AOA NLZGDHALQ EA HACOGURFMD. ETWRHN IKU BRWTU WHRKS YRD WDQS ADQFUSV, MO FXLTQPDC YINQ MKR GZMOGFU MEISEIWMRZ XERDE DGCO RD IULUTQUO AES WUOAETI EA QMF ZU KSFOKQKHAO HCGQTUSW CCG KPIUGWGE IUEAMRT. QANAWUQABUDDX, PG OMTBGWOUGE QMCR QMKR ZGTW IEUZOBWRYD OIU KUOOMFBUDO, MF HIWR, DC QPG OREG NWIROBAKOKYD EA NMOFU, ZABQUIGWRULO TFUWAETMYRABQ EA IKR XAWM. IKR ZGTW UZKBMA FBPHIRNH RD ICPL IKX KLWLIT KAWL ZLZUFBQHWD, UG AL-WGAL’U TQUIWRUL FSQ MKR AOA, VOPNQGE ELVA PGNWKOZ TIEH QKR UOUZRCRMGA BR C IBA EA QMF UGLKEO FCG PG DGCU WDQS ADQFUSW C EGPFCRGE ICH. QO PQ XOUD TTFK VIGHKHN QMCR IKT SDFGFSDW TGFOZGE IEUZOBWRYD, ADKCHAGE ORQM B RDIOZINY TAWG EKRATLZDU FIUFBO RD QMG PHOPGTU FRQMAWMRPOR, XKOO BNMPOZG IKR BKPR XMRIGQU EGCQHAD QPG FTSWUOCQ GFQMQTRITK EA QMD FWAYOT. UD RINU DCG PG WHOZQ KKR AESUMNDIHAE HWRWNUD PDDUHAO VMRM QPG IULUMOGFR CQ KKR OBTU FLTU NMBAFD EA PDDUHAN QKR IRKT. QMCR OIT UPG FBQTG LN PKR IWEQPDCQ ORQM QMF UWRPD PKAHTUOU, VIA, RY TQTS CL UIRG, MBR RLPD TXPHCRMV ORQM OMBMGFU’ KLRMRRAA. HR MQ BDR GADX QMG DMROUIWW CSUKRR YIG TQBZPFST AUDI QMFPS, CQU BORL QML ZGFOHFGOU, EGRKNHOU BAE GCQUOIUGFFZS, TD RPG IUKPD PHAKRUDW RQ XOUV MFIMZ AET AINSOLU RD USD YD AINHND UPG IDLE HA OIQKHADQGA GA QMKR RDHKB. TUFBIHAO LA PCGQTUSRID SPGCU, M RQSC QD RPG ICSYUDW AC PKODGW ICG WAPLTKMRI VIG ICX CL ZGFEGNWERWRHN RD TUOFD LQS KEBAR. K FBBVAGY CDUOUPKFG GA QML FBRKR EA QMD PLURBOGR XIKNM ZO INZG EGAMHIOUGE VIDUPGS UPGW CUO OASIHAO VMRM QPG PS SBSZ SBBA RD QFEGTIHAG LQS KEBAT LRWDFSDW, DW RC UPGRW HAUDUOTUR BUO GFRMUODX ADKYPDTARIE. KOUINKU QMDZ IWG PEIHAD QL RGDD SPG EGRKNHR, LS UD IBAZPBFUQUO WRWND KBFIKFGR BCG EAPFS UPGI CR C FTU MWRFD RD QMG OGWOUCHGFR. MCGLZGE, QMOUD FERDE FL I OMOOU ICSIDU EA OLZGQAPDCQR BCG AWONAHRBRMGAR XIG OASEO TGDKRI N UOFGZOO CAKOKYD RD IDAHRDS UPG ADKYPTAHFBRMGAR LC UPGRW WRWNBX, BAO MR YERDE BDOFSOV CDR FL HA ERW RCQOULUUT RD BODLO AQS UDNMAGDLDV RD NBBLO KCQD RPGRW INCGU. LUKDFRIBLDX AGS CFPAWO ZG PNWO UOFNMGE BA NOUODPGFR YMRM QPG OLZGQAPDCQ GA QMOPU OQMMABO QTO. PA ZD PHOMQ QFADZGS UPG MOGFRMYD EA WAPLTKMRI VD PCW FL FLSYUDW IKBD UL EKRFDQA VIMAI GC UPGUL IEXLRKAKOKRMLU KR IDUO OKPLDX AW CR DGBRR CMY RD OMTSZUQ MKR AW PGW RCQGFRMGAT. XERST DUF, CBCCBOG")
    
    iterations = 10000
    threshold = 0.03
    margin = 0.03
    
    operations = [SwapElements, SwapRow, SwapColumn, FlipVertically, FlipHorizontally, FlipDiagonally]
    #operations = [SwapElements]
    
    #parent_key = KeyWithSwaps("abcdefghiklmnopqrstuvwxyz", 26)
    parent_key = "abcdefghiklmnopqrstuvwxyz"
    parent_plaintext = ciphertext
    parent_fitness = GetFitness(ciphertext)
    
    counter = 0
    while counter < iterations:
        operation = random.choice(operations)
        child_key = operation(parent_key)
        child_plaintext = DecodeWithKey(ciphertext, child_key)
        child_fitness = GetFitness(child_plaintext)
        
        if (child_fitness < parent_fitness) or (child_fitness < (parent_fitness + margin) and random.randint(1, 20) == 20 and child_key != parent_key) :
            parent_fitness = child_fitness
            parent_key = child_key
            parent_plaintext = child_plaintext
            print(
                f"Iterations: {counter:3} | Fitness: {round(parent_fitness, 3):5} | Key: {parent_key} | Plaintext: {parent_plaintext[:20]} | IoC: {round(IndexOfCoincidence(parent_plaintext), 3):5}")
            counter = 0
            
        
        counter += 1
    
    print(parent_plaintext)
        
        
        
        

if __name__ == " __main__":
    key = "abcdefghiklmnopqrstuvwxyz"
    key = FlipDiagonally(key)
    print(key)
        
    
    
    