import numpy as np
import sys

def check_valid_csv(df):
    valid_numeric_types = ['int32', 'int64', 'float32', 'float64']

    for column in df.columns:
        column_type = df[column].dtype
        if column_type.name not in valid_numeric_types:
            raise ValueError(f"Column '{column}' is NOT of valid numeric type. It is of type {column_type}.")

    print("CSV file is valid.")

def normaise_df(df):
    for column in df.columns:
        df[column] = df[column] / np.sqrt(np.sum(df[column] ** 2))
    return df

def weight_adjusted_normalise_df(df,weights):
    cols = df.columns
    for i in range(len(df.columns)):
        df[cols[i]] = df[cols[i]] * weights[i]
    return df

def add_ideal_vals(df,impact):
    ideal_best = []
    ideal_worst = []
    for i in range(len(df.columns)):
        if impact[i] == '+':
            ideal_best.append(max(df[df.columns[i]]))
            ideal_worst.append(min(df[df.columns[i]]))
        elif impact[i] == '-':
            ideal_best.append(min(df[df.columns[i]]))
            ideal_worst.append(max(df[df.columns[i]]))
    df.loc[len(df)] = ideal_best
    df.loc[len(df)] = ideal_worst
    return df



def find_euclidean_distances(df):
    numeric_df = df.select_dtypes(include=[np.number])

    last_row = numeric_df.iloc[-1].to_numpy()
    second_last_row = numeric_df.iloc[-2].to_numpy()

    df['euclidean_distance_worst'] = numeric_df.apply(
        lambda row: np.linalg.norm(row.to_numpy() - last_row), axis=1
    )
    df['euclidean_distance_best'] = numeric_df.apply(
        lambda row: np.linalg.norm(row.to_numpy() - second_last_row), axis=1
    )
    
    return df

def performance_score(df):
    df['performance_score']= df['euclidean_distance_worst'] / (df['euclidean_distance_best'] + df['euclidean_distance_worst'])
    return df

def give_rank(df):
    df = df.drop(df.index[-2:])
    df['rank'] = df['performance_score'].rank(ascending=False, method='dense').astype(int)
    return df

def save_to_csv(df, filename):
    df.to_csv(filename, index=False)


def run(df, weights, impact, output):
    check_valid_csv(df)
    normalised_df = normaise_df(df)
    weighted_normalised_df =weight_adjusted_normalise_df(normalised_df,weights)
    idiolilsed_w_n_df = add_ideal_vals(weighted_normalised_df, impact)
    euclidian_distance_df = find_euclidean_distances(idiolilsed_w_n_df)
    performance_score_df = performance_score(euclidian_distance_df)
    ranked_df = give_rank(performance_score_df)
    save_to_csv(ranked_df, output)
    print(ranked_df)