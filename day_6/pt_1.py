# Preston Beaty
# Advent Day 6 Challenge
# Dec 6th, 2022

import os

def allUnique(x):
    seen = set()
    return not any(i in seen or seen.add(i) for i in x)

input = "pfptpztzfznzzznszzfgzgqgbgzgmzggwlwnlngnddjttzwtwmttlrrlqqzczpzhppmjmnjnfjnjjjprpfpnfpnpznzbbnwbbdsbswwwwszzzcmcttbftffczctztffppcvccbdbhbtbcbhbrbnrbrzbztbblvlvqvcqvcvcrcprrmffhfwfjwjrjtttvqqsttcwtthwthhqssbbqhhcbhbhqqwsqspqspprbrsrmmvhvvlsvspvpddbvdbdhhgshggfbgbrggzszsnshsvhsvhhnfnhfnhhbzzthtstdssdsrdsrdrtddsrdrcrgcgdcggdbbtgbgzbzwwnlngggspggspspjjfqflqqttjbbnffszfzjjlwjwhjwjccpllzztrzttdpdbbcnntwnnctnnrrgbrbvbccvzvlvnllvrvnnvmmtrmrddjdqdrqrmmvssgllsjsrrwggvcccgwwgddzldzldzdttqrrtggdngdgfdgfgzztdtthrttszzgjglldzdhdphppjfjfzfpfsflfggpwwwjdjssqdqmdmdpmmvbvfvpfpfwfpwfppbgbwgbbpmpwpzplpjpttnwnlnppcvchhmwwmllwppwspwspswpphhdhfhccwpcplpzzjwjssfrsssgnglnglnglngncgcvvpddrcrjrssznnjllslrlmllglpggwhhllzqzssvtsvvbpphpthphdhphnhdhdqdbbmcmqcmcmddtwtqqsbbzddtzdzrzmmfccdttlvljlffzczmzrrtzzrbrllfnfmfnnrcnnctcnnncbcrbccwcnwcnnrbnrrpnprrtwwvcwchwwcbwwwnpnvvgtvvqmvvhttrnnvjjtwtfwtwrrbpbmbmzmpphwphwwqwgwlwclwccjvccsllhhrtrstthvvfjjcvcdcbdcbczcttjbttwtvvvzjzgzwgwjjsnnvrrlbrrvnvdvhvchvvglvvpssdbsszddsqsspvpbpjjgghvvlwvlvggpjjmcjmmmhjmmrgrsgrsggchhcmmqsmsttlslqqmjjbpbrrcnrnbbvqvsvtvftvtmmqzzsnscsffnrnmrmnnszsllsrrrzrszsbbchccsrsmshhzrhrrdlrrjfmlrfhvqqvmpbrntgcqqsqvjmtctflbffddfbsjvzsfdwblprszhfvltwtcfsbdlwjgsmlcrvgstjqtrtnqzbmrmgqnscqjdfnbppcdgcsstwdmdvphsqmrfmzwntjgjjvcdgbhfjqlzglgjdsdlhwwrmfqcfsvhwwfmvprpnmjppvwzjwmddtndspzqjqrpbpnrjfwqfvbtqrgngcbjvhnfbtslcpppbsfhbcmwgpccftwhnbvdrzqdtwnrtjcdlnlmhvlzvljwrzgtfjrpgzjvggtpsvcdgtsvhdzvtfbwmnptfmllgcvfmmgvpbrgnhcnpwltqmjmltsbpzmfrttsmjqwhncvtqrsmcpsnrqzmwftbltllbhzhdfzmfgbvdtgwpvngsffjmwhfhmccfrjgqcqngzlnqvsgrcdzbsmjbmflwvhjldlrdvjrmgvjvpcczdhczpbtwphvhqmhcnljbwnzqwmbctffmctlcmhzcnvprdhtzdvgbhlnnjqzcwcsrgzjjlszssnplwqjlczvftmnbnmdpbjnctnslhgsjswqjwvprdstvbstlnnwwgvsffwmprjrlfccmtgvqbghvhcngwwtzwbwcdmrfstwhtfghgvzbfgtwjglcllwrhgdzptvrrbdhbscjhmtswshjmrsbpzstwmhrwwwncbbmjnjjlzrpdrzfvstbltszvlhcqbcpgbwtzzslsrljmhmtlcvzdbszvnjhrswrjrmfpsfpplwlrsnrpnjngmhwpwqcmtslhbmlsmjhcgmzznftmhvtmzlvmcwnbqtcntqghrqcsztsgzrnmrlvrnhtpmstdflpztmwltvgppttfwhhzzgrffjchswhbljvcjwvvnqnvdvjpsclhwsrtczvjmtcsnwvnwtdllphmrthddfvcjwvggqltmhglllmqzjsbjwgdqwzzmjnrmpbqplgzjgzcdqmtsntprdwwjwthcbsghqqspszndgqdmlzdlzwfcghtbhcqpbpmnfgqzmhtnttvjttvzhllsjvmmcmmppcgssjhnzqwpzdbtmrzsfbvgmgbtbwjrzvdlmgjpzltfmcclpltsszpqbllrwbwsnbhhvfwphrcpdvbjhgmgpphrdpcmjvfsjzrqldlqthwsztzcgttdnzcsbnszcsvmcspddlmwjttggdmlpqrdrfmwfzpdbnrwtmwssvbwtmzhndmhzwtlgdwpbrzghmlbszswqlpzldbvswjgtvjvmtjwdggfsbggbwhpwjdmflhmsgtbzrtbvlpqqmpcrbhflnfmwwsvdsgnnznfrqhqgqfgdfzcdqrtdftsntpbcclhncqjjwvszmssswnscwjlpfvdvltgcmqqttnfvbptbbmlrvrwwfbwwbvlrdrfmscqwdvdjgdrghwfjsttvwngzttzzsmzqnvzdfsvrbrcwtmmjdvnzjzdsnzgtszzcwdphnjmspmdsrqwgdwlzrgghcchpbltmwnjrbhqhzdqqmbrpggjjwnqfnnsqsfzbwqjsfprvrvfwbqvhgpjvqzplnhtqszqrtsvtbptfvzmvjhshbtmqbmqrrwplzphvdvhttlmftdwltqssstzlvnslzhnmjdlsbdprbgpjvcdtcfchzqqqcnngbrmntjwfbvcdcfgbcpnvcbbcvhqfzpsmgbcvrqvjlqlqnvvzdgphfpgtrpbbwztvqjgdpnpwbffdgqzmqvgblwzmdrhwdprhcqppcggrldhcdztnhspclfcwttnqslnzvvshcwgfztvscvztdrprvnlmfsgcpfdmfjgblnhrbsmjrjdzjwvwmlllvscsvfqvhdsdljrqphcvvtcttbwvnwwzwshdcfdqnjszltmddzjgmqgvpjzpzssrmfsrgjhvqtlhsfnndnqhpbcnltmdvlhfwqcmwnqbhsfqqwnfnnfjjbsqmcdrrvlfztdprnmjfhlvcdbjtczbrpljmpcwvchdwrqbwggjnrlhcdgzfwjzzjgfnbpwbpvswqdpcrthwfcffgztrjqntczfcbsrrtrjrwgbbgjshtzvjjlqqtsbgmpsttqjqwgmmbzhshqvvrcgbdsqmtqlrgjbnvbrpzdrgqnzstfdcvdnjhcnjblmsqtfvstlptgrczhbgpllpqwfdmthgjlltmlnltzpvjvjfgtrzslsptlfplgrgpjsbhbbbwlljfdjnhqcndlprfbwpvddndpnqwqccgbqmwlrffpzjpqclwcrgjgljwzpppwltcwdqdchghfnwbhrjndjsvlqnnmlrjfgfpnvgmlhbgnhnztpjzdmltfmjtzclsbspvhfngtjmzwrwmprdfplzzwfrdnbmbgvjlczcdvmpfmtqmzjrpfhjwwzmtnzmptwnhtlbndcpshqrqqrpccqpnvnqqdprvccmdmrsbptdhrhlpcptgfsfwphfpvbcrlnbrtgwcpgjclhhvpjhcwcgghlzbmpbswgtzqhmlwdfrrdfvnbhlqhvhnfjfndlqgrvhwnnnccvgdfqtwlmbwcpdtgscfpvmbdtcdmmgqrfjvnhngqsdtzhlbjwrrcrjfswwrgbhznlwhcjlsfprbqqcqmbdjhgjmmtqmjpldgqvptqcwjmlrjtjwdfbbvhpsnmfvdwnrntqzhfgfmrtgwgddpqvvdjqvrdwdwrsbjlbrmrjjbbpjpqgsjdzfjcrsnbmtmrstcrztzhgswgghwbfltdsvrcqvvjtmjwznnnwtsmshvbbpzwltrjpmbgsbqwphmwlhgpltsgjmgbdfrlhcbfjnvpvdwzccgdhswtgplcqnsjdwfbhbbpssvfrjbzmcphzjdncjgsvrcrplhqpnwdgfvrjqgfshdwrqjdvjmggtnnghqrccgddnzndcgpgpghtvrpwftfpttvgwqqcjbvnmqzlshdrdj"

for i in range(len(input)):
    uniq_check = [input[i], input[i+1], input[i+2], input[i+3]]
    
    if (allUnique(uniq_check)):
        print("First Marker after: ", (i+4))
        break