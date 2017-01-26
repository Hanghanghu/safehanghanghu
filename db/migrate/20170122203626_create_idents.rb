class CreateIdents < ActiveRecord::Migration
  def change
    create_table :idents do |t|

      t.timestamps
    end
  end
end
