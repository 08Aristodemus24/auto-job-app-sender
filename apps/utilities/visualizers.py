import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os
import seaborn as sb

def view_rows(df: pd.DataFrame, column: str):
    for _, row in df.iterrows():
        print(row[column])

def view_all_splits_results(history_dict: dict, save_img: bool=True, img_title: str="untitled", style: str='dark'):
    """
    
    """
    styles = {
        'dark': 'dark_background',
        'solarized': 'Solarized_Light2',
        '538': 'fivethirtyeight',
        'ggplot': 'ggplot',
    }
    plt.style.use(styles.get(style, 'default'))

    # create the history dataframe using tensorflow history attribute
    history_df = pd.DataFrame(history_dict)
    print(history_df)

    palettes = np.array(['#f54949', '#f59a45', '#afb809', '#51ad00', '#03a65d', '#035aa6', '#03078a', '#6902e6', '#c005e6', '#fa69a3', '#240511', '#052224', '#402708', '#000000'])
    markers = np.array(['o', 'v', '^', '8', '*', 'p', 'h', ])#'x', '+', '>', 'd', 'H', '3', '4'])

    sampled_indeces = np.random.choice(list(range(len(markers))), size=history_df.shape[1], replace=True)

    print(palettes[sampled_indeces])
    print(markers[sampled_indeces])

    figure = plt.figure(figsize=(15, 10))
    axis = sb.lineplot(data=history_df, 
        palette=palettes[sampled_indeces].tolist(),
        markers=markers[sampled_indeces].tolist(), 
        linewidth=1,
        markersize=3.5,
        alpha=0.75)
    
    axis.set_ylabel('metric value', )
    axis.set_xlabel('epochs', )
    axis.set_title(img_title, )
    axis.legend()

    if save_img == True:
        save_dir = f"./figures & images"
        os.makedirs(save_dir, exist_ok=True)

        file_path = os.path.join(save_dir, f"{img_title}.png")
        plt.savefig(file_path)
        plt.show()

class ModelResults:
    def __init__(self, history, epochs, style: str='dark'):
        """
        args:
            history - the history dictionary attribute extracted 
            from the history object returned by the self.fit() 
            method of the tensorflow Model object 

            epochs - the epoch list attribute extracted from the history
            object returned by the self.fit() method of the tensorflow
            Model object
        """
        self.history = history
        self.epochs = epochs
        self.style = style

    def _build_results(self, metrics_to_use: list):
        """
        builds the dictionary of results based on history object of 
        a tensorflow model

        returns the results dictionary with the format {'loss': 
        [24.1234, 12.1234, ..., 0.2134], 'val_loss': 
        [41.123, 21.4324, ..., 0.912]} and the number of epochs 
        extracted from the attribute epoch of the history object from
        tensorflow model.fit() method

        args:
            metrics_to_use - a list of strings of all the metrics to extract 
            and place in the dictionary
        """

        # extract the epoch attribute from the history object
        epochs = self.epochs
        results = {}
        for metric in metrics_to_use:
            if metric not in results:
                # extract the history attribute from the history object
                # which is a dictionary containing the metrics as keys, and
                # the the metric values over time at each epoch as the values
                results[metric] = self.history[metric]

        return results, epochs
    
    def export_results(self, dataset_id: str="untitled", metrics_to_use: list=['loss', 
                                            'val_loss', 
                                            'binary_crossentropy', 
                                            'val_binary_crossentropy', 
                                            'binary_accuracy', 
                                            'val_binary_accuracy', 
                                            'precision', 
                                            'val_precision', 
                                            'recall', 
                                            'val_recall', 
                                            'f1_score', 
                                            'val_f1_score', 
                                            'auc', 
                                            'val_auc'], save_img: bool=True):
        """
        args:
            metrics_to_use - a list of strings of all the metrics to extract 
            and place in the dictionary, must always be of even length
        """

        # extracts the dictionary of results and the number of epochs
        results, epochs = self._build_results(metrics_to_use)
        results_items = list(results.items())

        # we want to leave the user with the option to 
        for index in range(0, len(metrics_to_use) - 1, 2):
            # say 6 was the length of metrics to use
            # >>> list(range(0, 6 - 1, 2))
            # [0, 2, 4]
            metrics_indeces = (index, index + 1)
            curr_metric, curr_metric_perf = results_items[metrics_indeces[0]]
            curr_val_metric, curr_val_metric_perf = results_items[metrics_indeces[1]]
            print(curr_metric)
            print(curr_val_metric)
            curr_result = {
                curr_metric: curr_metric_perf,
                curr_val_metric: curr_val_metric_perf
            }
            print(curr_result)

            self.view_train_cross_results(
                results=curr_result,
                epochs=epochs, 
                curr_metrics_indeces=metrics_indeces,
                save_img=save_img,
                img_title="model performance using {} dataset for {} metric".format(dataset_id, curr_metric)
            )

    def view_train_cross_results(self, results: dict, epochs: list, curr_metrics_indeces: tuple, save_img: bool, img_title: str="untitled"):
        """
        plots the number of epochs against the cost given cost values 
        across these epochs.
        
        main args:
            results - is a dictionary created by the utility preprocessor
            function build_results()
        """
        styles = {
            'dark': 'dark_background',
            'solarized': 'Solarized_Light2',
            '538': 'fivethirtyeight',
            'ggplot': 'ggplot',
        }

        plt.style.use(styles.get(self.style, 'default'))

        figure = plt.figure(figsize=(15, 10))
        axis = figure.add_subplot()

        styles = [
            ('p:', '#f54949'), 
            ('h-', '#f59a45'), 
            ('o--', '#afb809'), 
            ('x:','#51ad00'), 
            ('+:', '#03a65d'), 
            ('8-', '#035aa6'), 
            ('.--', '#03078a'), 
            ('>:', '#6902e6'),
            ('p-', '#c005e6'),
            ('h--', '#fa69a3'),
            ('o:', '#240511'),
            ('x-', '#052224'),
            ('+--', '#402708'),
            ('8:', '#000000')]

        for index, (key, value) in enumerate(results.items()):
            # value contains the array of metric values over epochs
            # e.g. [213.1234, 123.43, 43.431, ..., 0.1234]

            if key == "loss" or key == "val_loss":
                # e.g. loss, val_loss has indeces 0 and 1
                # binary_cross_entropy, val_binary_cross_entropy 
                # has indeces 2 and 3
                axis.plot(
                    np.arange(len(epochs)), 
                    value, 
                    styles[curr_metrics_indeces[index]][0], 
                    color=styles[curr_metrics_indeces[index]][1], 
                    alpha=0.5, 
                    label=key, 
                    markersize=5, 
                    linewidth=1.5)
            else:
                # here if the metric value is not hte loss or 
                # validation loss each element is rounded by 2 
                # digits and converted to a percentage value 
                # which is why it is multiplied by 100 in order
                # to get much accurate depiction of metric value
                # that is not in decimal format
                metric_perc = [round(val * 100, 2) for val in value]
                axis.plot(
                    np.arange(len(epochs)), 
                    metric_perc, 
                    styles[curr_metrics_indeces[index]][0], 
                    color=styles[curr_metrics_indeces[index]][1], 
                    alpha=0.5, 
                    label=key, 
                    markersize=5, 
                    linewidth=1.5)

        # annotate end of lines
        for index, (key, value) in enumerate(results.items()):        
            if key == "loss" or key == "val_loss":
                last_loss_rounded = round(value[-1], 2)
                axis.annotate(last_loss_rounded, xy=(epochs[-1], value[-1]), color='black', alpha=1)
            else: 
                last_metric_perc = round(value[-1] * 100, 2)
                axis.annotate(last_metric_perc, xy=(epochs[-1], value[-1] * 100), color='black', alpha=1)

        axis.set_ylabel('metric value', )
        axis.set_xlabel('epochs', )
        axis.set_title(img_title, )
        axis.legend()

        if save_img == True:
            save_dir = f"./figures & images"
            os.makedirs(save_dir, exist_ok=True)

            file_path = os.path.join(save_dir, f"{img_title}.png")
            plt.savefig(file_path)
            plt.show()

        # delete figure
        del figure