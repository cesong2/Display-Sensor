import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

error = pd.read_csv("/archive/PdM_errors.csv")
failures = pd.read_csv("/archive/PdM_failures.csv")
machines = pd.read_csv("/archive/PdM_machines.csv")
maint = pd.read_csv("/archive/PdM_maint.csv")
telemetry = pd.read_csv("/archive/PdM_telemetry.csv")