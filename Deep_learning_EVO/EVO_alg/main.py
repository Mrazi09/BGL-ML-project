import logging
from optimizer import Optimizer
from tqdm import tqdm
from train_siganl2 import get_data

# Setup logging.
logging.basicConfig(
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%m/%d/%Y %I:%M:%S %p',
    level=logging.DEBUG,
    filename='log_Multilabel.txt'
)

def train_networks(networks, dataset):
    """Train each network.
    Args:
        networks (list): Current population of networks
        dataset (str): Dataset to use for training/evaluating
    """
    pbar = tqdm(total=len(networks))
    for network in networks:
        network.train(dataset)
        pbar.update(1)
    pbar.close()

def get_average_accuracy(networks):
    """Get the average accuracy for a group of networks.
    Args:
        networks (list): List of networks
    Returns:
        float: The average accuracy of a population of networks.
    """
    total_accuracy = 0
    for network in networks:
        total_accuracy += network.accuracy

    return total_accuracy / len(networks)

def generate(generations, population, nn_param_choices, dataset):
    """Generate a network with the genetic algorithm.
    Args:
        generations (int): Number of times to evole the population
        population (int): Number of networks in each generation
        nn_param_choices (dict): Parameter choices for networks
        dataset (str): Dataset to use for training/evaluating
    """
    optimizer = Optimizer(nn_param_choices)
    networks = optimizer.create_population(population)

    # Evolve the generation.
    for i in range(generations):
        logging.info("***Doing generation %d of %d***" %
                     (i + 1, generations))

        # Train and get accuracy for networks.
        train_networks(networks, dataset)

        # Get the average accuracy for this generation.
        average_accuracy = get_average_accuracy(networks)

        # Print out the average accuracy each generation.
        logging.info("Generation average: %.2f%%" % (average_accuracy * 100))
        logging.info('-'*80)

        # Evolve, except on the last iteration.
        if i != generations - 1:
            # Do the evolution.
            networks = optimizer.evolve(networks)

    # Sort our final population.
    networks = sorted(networks, key=lambda x: x.accuracy, reverse=True)

    # Print out the top 5 networks.
    print_networks(networks[:5])

def print_networks(networks):
    """Print a list of networks.
    Args:
        networks (list): The population of networks
    """
    logging.info('-'*80)
    for network in networks:
        network.print_network()

def main():
    """Evolve a network."""
    generations = 5  # Number of times to evole the population.
    population = 10  # Number of networks in each generation.
    dataset = get_data('/media/joao/EXTERNAL_USB/1-BGL-ML_roots/data_with_JetMatching/Data_EVO/X_train_314p99.npz','/media/joao/EXTERNAL_USB/1-BGL-ML_roots/data_with_JetMatching/Data_EVO/X_test_314p99.npz', \
                  lumi=3000., sig_xs=0.006401310579384756, bg_xs=[0.04545909812729102,2.4173040583264083,6.220919700960317,0.02371859429217693,9.638496115803719],
                  systematic=0.01)

    nn_param_choices = {
        'nb_neurons': [256, 512, 1024, 2048],
        'nb_layers': [1, 2, 3, 4, 5],
        'initializer':['normal','he_normal','he_uniform'],
        'alpha':[1e-3,1e-5,1e-7],
        'activation': ['relu', 'elu', 'tanh', 'sigmoid'],
        'optimizer': ['adam', 'sgd', 'adamax', 'nadam'],
    }

    logging.info("***Evolving %d generations with population %d***" %
                 (generations, population))

    generate(generations, population, nn_param_choices, dataset)

if __name__ == '__main__':
    main()
