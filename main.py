import os
from apis.Pin_PhiUSIIL_api import PhiUSIILManager
from apis.Pin_forest_api import pinforest
from apis.Pin_PhiSNAIL_api import PhiSNAILAssistant
from apis.Pin_security_api import SecurityManager
from apis.Pin_ai_api import JobMarketInsights
from apis.Pin_supermarket_api import SupermarketManager
from apis.Pin_arcd_api import ARCDManager
from apis.Pin_sales_api import SalesManager
from apis.Pin_marketing_api import MarketingManager
from apis.Pin_technical_support_api import TechnicalSupportManager
from apis.Pin_customer_support_api import CustomerSupportManager
from apis.Pin_inventory_api import InventoryManager
def main():
    # Initialize the project managers
    pin_phiUSIIL = PhiUSIILManager()
    pin_forest = pinforest()
    pin_phiSNAIL = PhiSNAILAssistant()
    pin_security = SecurityManager()
    pin_ai_job_market_insights = JobMarketInsights()
    pin_supermarket = SupermarketManager()
    pin_arcd = ARCDManager()
    pin_sales = SalesManager()
    pin_marketing = MarketingManager()
    pin_technical_support = TechnicalSupportManager()
    pin_customer_support = CustomerSupportManager()
    pin_inventory = InventoryManager()

    # Load data
    data_path = 'data/raw/PhiUSIIL_Phishing_URL_Dataset.csv'
    if os.path.exists(data_path):
        pin_phiUSIIL.load_data(data_path)
    else:
        print(f"Data file not found at {data_path}. Please check the path.")

    # Initialize other components
    pin_phiUSIIL.initialize_project()
    pin_phiSNAIL.initialize_assistant()
    pin_security.initialize_security()
    pin_ai_job_market_insights.initialize_insights()
    pin_supermarket.initialize_supermarket_management()
    pin_arcd.initialize_arcd()
    pin_sales.initialize_sales()
    pin_marketing.initialize_marketing()
    pin_technical_support.initialize_technical_support()
    pin_customer_support.initialize_customer_support()
    pin_inventory.initialize_inventory_management()

    # Start the main workflow
    pin_phiUSIIL.run_workflow()

if __name__ == "__main__":
    main()
    
    