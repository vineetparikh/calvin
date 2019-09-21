import json
from dataeng import vectorize_from_github_name, convert_number_to_value, convert_value_to_number
from sklearn import svm
import argparse

clf = svm.SVC()

def train_model():
    train_github_vecs = []
    train_results = []
    with open('training_data.json') as json_file:
        data = json.load(json_file)
        for pair in data["package-scores"]:
            github_vec = vectorize_from_github_name(pair["name"])
            train_github_vecs.append(github_vec)
            train_val = convert_value_to_number(pair["value"])
            train_results.append(train_val)
    clf.fit(train_github_vecs,train_results)

def apply_model(name): # returns number from 0 to 1 representing
# likelihood that repo will be continually maintained and existing
# vulnerabilities will be fixed
    github_vec = vectorize_from_github_name(name)
    result = clf.predict([github_vec])
    retval = convert_number_to_value(result[0])
    return retval

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-o','--orgname',dest='orgname',default=None,help='Organization name (such as "keras-team" for keras)')
    parser.add_argument('-r','--repname',dest='repname',default=None,help='Repository name (such as "keras" for keras)')
    return parser.parse_args()

def main():
    options = parse_args()
    orgname = options.orgname if options.orgname is not None else raw_input('Organization name (such as "keras-team" for keras)')
    repname = options.repname if options.repname is not None else raw_input('Repository name (such as "keras" for keras)')
    name = orgname+"/"+repname

    train_model()
    print("Evaluation of "+name+": (Bad=low likelihood of being fixed/having a solid community, Good=highly active community):")
    print(apply_model(name))

if __name__ == '__main__':
    main()
